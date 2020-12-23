import matplotlib.pyplot as plt
import numpy
import pandas as pd
import scipy
import seaborn as sns

from scipy.stats import zscore
import statsmodels.api as sm
from statsmodels.formula.api import ols

from analysis import BehavioralSubjective
from config import ROOT_DIR

plt.rcParams.update({'font.size': 24})
plt.rcParams['font.family'] = 'Calibri'

graph_label = dict(color='#101010', alpha=0.95)


def plot_ba_subj_rating(df, ba, activation=True, participant=None):
    color = "#1f78b4"

    ax1 = df.plot(kind='scatter', x='subj_complexity', y=ba, s=50, c=color, figsize=(7, 5))
    z = numpy.polyfit(df['subj_complexity'], df[ba], 1)
    p = numpy.poly1d(z)

    plt.plot(df['subj_complexity'], p(df['subj_complexity']), linewidth=1)

    if activation:
        plt.ylabel("Activation in %\n" + ba)
    else:
        plt.ylabel("Deactivation in %\n" + ba)

    plt.xlabel("Subjective Complexity Rating")

    corr = df['subj_complexity'].corr(df[ba], method='kendall')
    print('subj_complexity: ~  BA: ' + ba)
    print('Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['subj_complexity'], df[ba])
    print('r squared:', r_value ** 2)

    left, right = plt.xlim()
    bottom, top = plt.ylim()
    ax1.text(left + ((right - left) / 40), bottom + ((top - bottom) / 8), 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left + ((right - left) / 40), bottom + ((top - bottom) / 40), 'r squared: ' + format(r_value ** 2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    if activation:
        prefix = ROOT_DIR + '/analysis/output/act_subj_'
    else:
        prefix = ROOT_DIR + '/analysis/output/deact_subj_'

    if participant:
        prefix += participant + '_'

    plt.savefig(prefix + ba + '.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.clf()


def plot_ba_for_metric(df, metric, ba, activation=True):
    color = BehavioralSubjective.select_color_for_metric(metric)

    fig = plt.figure(figsize=(7, 6))

    z = numpy.polyfit(df[metric], df[ba], 1)
    p = numpy.poly1d(z)

    plt.scatter(df[metric], df[ba], s=150, c=color)

    plt.plot(df[metric], p(df[metric]), linewidth=6, alpha=0.7)

    #plt.ylim((0, 61))

    if metric == "LOC":
        if activation:
            if ba is "BA44":
                plt.ylabel("Activation in %\nBroca")
            else:
                plt.ylabel("Activation in %\n" + ba)
        else:
            plt.ylabel("Deactivation in %\n" + ba)
    else:
        plt.ylabel("")

    if ba is "BA44":
        plt.xlabel(metric, color=color)
    else:
        plt.xlabel("")

    corr = df[metric].corr(df[ba], method='kendall')
    print('Metric: ' + metric + ' ~  BA: ' + ba)
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[metric], df[ba])
    print('-> r squared:', r_value ** 2)

    axes = plt.gca()
    if activation:
        #axes.set_yticks([0.5, 1, 1.5, 2, 2.5])
        #axes.set_ylim([0.5, 2.5])
        axes.set_yticks([1, 1.5, 2])
        axes.set_ylim([1, 2])
    else:
        axes.set_yticks([-0.5, -1, -1.5, -2, -2.5])
        axes.set_ylim([-0.5, -2.5])

    left, right = plt.xlim()
    bottom, top = plt.ylim()
    axes.text(left + ((right - left) / 40), bottom + ((top - bottom) / 7), 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    axes.text(left + ((right - left) / 40), bottom + ((top - bottom) / 40), 'r squared: ' + format(r_value ** 2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    if activation:
        prefix = ROOT_DIR + '/analysis/output/activation_'
    else:
        prefix = ROOT_DIR + '/analysis/output/deactivation_'

    plt.savefig(prefix + metric + '_' + ba + '.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.clf()
    plt.close(fig)


def get_bas(activation):
    if activation:
        #bas = ['BA6', 'BA21', 'BA39', 'BA45']
        bas = ['BA6', 'BA21', 'BA39', 'BA44']
    else:
        bas = ['BA32', 'BA31']

    return bas


def create_plots(df, snippet_metrics, activation=True):
    bas = get_bas(activation)

    # plot the stats
    for ba in bas:
        metrics = ["LOC", "DepDegree", "McCabe", "Halstead"]  # for a small run with the four main representatives
        metrics = list(snippet_metrics)[2:]  # for a full run

        for metric in metrics:
            plot_ba_for_metric(df, metric, ba, activation)


def compute_statistics(df, activation=True):
    bas = get_bas(activation)

    # OLS regression
    for ba in bas:
        print('\n\n### computing stats for ' + ba)
        result = ols(formula=ba + " ~ Halstead + McCabe + DepDegree", data=df).fit()
        print(result.summary())

        aov_table = sm.stats.anova_lm(result, typ=3)
        print(aov_table)


def compute_ba_subj_rating(activation=True):
    df_subj_complexity = pd.read_csv(ROOT_DIR + '/data/subjective/SnippetSubjectiveComplexityRatings.csv')
    if activation:
        df_ba_part_cond = pd.read_csv(ROOT_DIR + '/data/fMRI/fMRI_Analyzed_BA_Snippet_Participant_Activation.csv')
    else:
        df_ba_part_cond = pd.read_csv(ROOT_DIR + '/data/fMRI/fMRI_Analyzed_BA_Snippet_Participant_Deactivation.csv')

    df_ba_part_cond_subj = pd.merge(df_ba_part_cond, df_subj_complexity, left_on=['participant', 'Snippet'], right_on=['participant', 'snippet'])
    df_ba_part_cond_subj.sort_values(by='participant', inplace=True)

    bas = get_bas(activation)

    # now average across participants for a group result
    df_ba_part_cond_subj_act = df_ba_part_cond_subj.groupby(['snippet']).mean().reset_index()

    for ba in bas:
        plot_ba_subj_rating(df_ba_part_cond_subj_act, ba, activation)


def main():
    print('\n# Analyzing fMRI and complexity metrics data')
    df_ba_cond_act = pd.read_csv(ROOT_DIR + '/data/fMRI/fMRI_Analyzed_BA_Snippet_Activation.csv')
    df_ba_cond_deact = pd.read_csv(ROOT_DIR + '/data/fMRI/fMRI_Analyzed_BA_Snippet_Deactivation.csv')

    snippet_metrics = BehavioralSubjective.load_snippet_metrics()

    df_ba_cond_act = pd.merge(df_ba_cond_act, snippet_metrics, how='left', left_on=['condition'], right_on=['Snippet'])
    df_ba_cond_deact = pd.merge(df_ba_cond_deact, snippet_metrics, how='left', left_on=['condition'], right_on=['Snippet'])

    create_plots(df_ba_cond_act, snippet_metrics, True)
    create_plots(df_ba_cond_deact, snippet_metrics, False)

    compute_statistics(df_ba_cond_act, True)
    compute_statistics(df_ba_cond_deact, False)

    compute_ba_subj_rating(True)
    compute_ba_subj_rating(False)


if __name__ == "__main__":
    main()
