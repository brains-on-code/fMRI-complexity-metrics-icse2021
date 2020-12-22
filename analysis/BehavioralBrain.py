import numpy
import pandas as pd
import matplotlib.pyplot as plt

import BrainActivationAnalysis
from analysis import BehavioralSubjective

plt.rcParams.update({'font.size': 26})
import seaborn as sns
import scipy

# TODO this file is supposed to analyze complexity metrics versus behavioral data
graph_label = dict(color='#202020', alpha=0.9)

def plot_correlation(df, computeResponseTime, ba, activation=True):
    if computeResponseTime:
        variable = 'ResponseTime'
    else:
        variable = 'Correct'

    ax1 = df.plot(kind='scatter', x=variable, y=ba, s=50, figsize=(7, 4))
    z = numpy.polyfit(df[variable], df[ba], 1)
    p = numpy.poly1d(z)

    plt.plot(df[variable], p(df[variable]), linewidth=1)

    if computeResponseTime:
        plt.xlabel("Response Time (in sec.)")
    else:
        plt.xlabel("Correctness (in %)")

    if activation:
        plt.ylabel("Activation in %\n" + ba)
    else:
        plt.ylabel("Deactivation in %\n" + ba)

    corr = df[ba].corr(df[variable], method='kendall')
    print('Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[ba], df[variable])
    print('r squared:', r_value**2)

    left, right = plt.xlim()
    bottom, top = plt.ylim()
    ax1.text(left+((right-left)/40), bottom + ((top - bottom) / 7), 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left+((right-left)/40), bottom + ((top - bottom) / 40), 'r squared: ' + format(r_value**2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    if activation:
        pre = 'Activation_'
    else:
        pre = 'Deactivation_'

    plt.savefig('output/' + pre + ba + '_' + variable + '.pdf', dpi=300, bbox_inches='tight', pad_inches=0)


def compute_behavioral_brain(df_ba_cond, behavioral_data, activation):

    behavioral_ba = pd.merge(df_ba_cond, behavioral_data, how='left', left_on=['participant', 'Snippet'], right_on=['Participant', 'Snippet'])

    # check whether there is response times < 5s and exclude them since they are accidental clicks
    behavioral_ba["ResponseTime"].fillna(60000, inplace=True)
    behavioral_ba.loc[behavioral_ba['ResponseTime'] < 5000, 'ResponseTime'] = numpy.nan
    behavioral_ba = behavioral_ba.dropna(subset=['ResponseTime'])
    behavioral_ba["ResponseTime"] = behavioral_ba['ResponseTime'].apply(BehavioralSubjective.convert_to_second)

    # compute correct correctness
    behavioral_ba = behavioral_ba.groupby('Snippet').mean()
    behavioral_ba["Correct"] = behavioral_ba['Correct'].apply(BehavioralSubjective.convert_to_percent)

    for ba in BrainActivationAnalysis.get_bas(activation):
        plot_correlation(behavioral_ba, True, ba, activation)
        plot_correlation(behavioral_ba, False, ba, activation)


def main():
    df_ba_part_cond_act = pd.read_csv('../data/fMRI/fMRI_Analyzed_BA_Snippet_Participant_Activation.csv')
    df_ba_part_cond_deact = pd.read_csv('../data/fMRI/fMRI_Analyzed_BA_Snippet_Participant_Deactivation.csv')

    behavioral_data = BehavioralSubjective.load_behavioral_data()

    compute_behavioral_brain(df_ba_part_cond_act, behavioral_data, True)
    compute_behavioral_brain(df_ba_part_cond_deact, behavioral_data, False)

    print('\n##### \n-> all done \o/')


if __name__ == "__main__":
    main()
