#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns
import scipy

from config import ROOT_DIR

plt.rcParams.update({'font.size': 26})

graph_label = dict(color='#202020', alpha=0.9)


def load_snippet_metrics():
    print('\n##### \nread complexity metric data')
    snippet_metrics = pd.read_csv(ROOT_DIR + "/data/metrics/SnippetComplexityMetricsValues.csv", delimiter=",")
    snippet_metrics = snippet_metrics.astype('float', errors='ignore')
    print(snippet_metrics.head(5))
    return snippet_metrics


def load_behavioral_data():
    print('\n##### \nread behavioral data')

    behavioral_data = pd.read_csv(ROOT_DIR + "/data/behavioral/ParticipantBehavior.csv", delimiter=",")
    behavioral_data = behavioral_data.astype('float', errors='ignore')

    behavioral_data = behavioral_data[behavioral_data['Condition'] == "Comprehension"]

    print('-> found data of the following participants:', behavioral_data.Participant.unique())
    print(behavioral_data.head(5))

    return behavioral_data


def plot_correlation_correctness(df, metric):
    color = select_color_for_metric(metric)

    ax1 = df.plot(kind='scatter', x=metric, y='Correct', s=50, c=color, figsize=(7, 4))
    z = numpy.polyfit(df[metric], df['Correct'], 1)
    p = numpy.poly1d(z)

    plt.plot(df[metric], p(df[metric]), linewidth=1)
    plt.ylim((0, 101))

    if metric == "LOC":
        plt.ylabel("Correct Responses\n(in %)")
    else:
        plt.ylabel("")

    plt.xlabel(metric, color=color)

    corr = df[metric].corr(df['Correct'], method='kendall')
    print('Metric: ' + metric + ' ~  Correctness')
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[metric], df['ResponseTime'])
    print('-> r squared:', r_value**2)

    left, right = plt.xlim()
    ax1.text(left+((right-left)/40), 14, 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left+((right-left)/40), 1, 'r squared: ' + format(r_value**2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    plt.savefig(ROOT_DIR + '/analysis/output/' + metric + '_Correctness.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(plt.gcf())


def plot_correlation_responsetime(df, metric):
    color = select_color_for_metric(metric)

    ax1 = df.plot(kind='scatter', x=metric, y='ResponseTime', s=50, c=color, figsize=(7, 4))
    z = numpy.polyfit(df[metric], df['ResponseTime'], 1)
    p = numpy.poly1d(z)

    plt.plot(df[metric], p(df[metric]), linewidth=1)
    plt.ylim((0, 61))

    if metric == "LOC":
        plt.ylabel("Response Time \n (in seconds)")
    else:
        plt.ylabel("")

    plt.xlabel("")

    corr = df[metric].corr(df['ResponseTime'], method='kendall')
    print('Metric: ' + metric + ' ~  ResponseTime')
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[metric], df['ResponseTime'])
    print('-> r squared:', r_value**2)

    left, right = plt.xlim()
    ax1.text(left+((right-left)/40), 8, 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left+((right-left)/40), 1, 'r squared: ' + format(r_value**2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    plt.savefig(ROOT_DIR + '/analysis/output/' + metric + '_ResponseTime.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(plt.gcf())


def plot_correlation_subjcomplexity_metrics(df, metric):
    color = select_color_for_metric(metric)

    ax1 = df.plot(kind='scatter', x=metric, y='subj_complexity', s=50, c=color, figsize=(7, 5))
    z = numpy.polyfit(df[metric], df['subj_complexity'], 1)
    p = numpy.poly1d(z)

    plt.plot(df[metric], p(df[metric]), linewidth=1)
    plt.ylim((0, 100))

    if metric == "LOC":
        plt.ylabel("Subjective Complexity")
    else:
        plt.ylabel("")

    plt.xlabel(metric, color=color)

    corr = df[metric].corr(df['subj_complexity'], method='kendall')
    print('Metric: ' + metric + ' ~ SubjComplexity')
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df[metric], df['subj_complexity'])
    print('-> r squared:', r_value**2)

    left, right = plt.xlim()
    ax1.text(left+((right-left)/40), 10, 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left+((right-left)/40), 1, 'r squared: ' + format(r_value**2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    plt.savefig(ROOT_DIR + '/analysis/output/SubjComplexity_' + metric + '.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(plt.gcf())


def plot_correlation_subjcomplexity_responsetime(df):
    ax1 = df.plot(kind='scatter', x='subj_complexity', y='ResponseTime', s=30, figsize=(7, 5))
    z = numpy.polyfit(df['subj_complexity'], df['ResponseTime'], 1)
    p = numpy.poly1d(z)

    plt.plot(df['subj_complexity'], p(df['subj_complexity']), linewidth=1)
    plt.xlim((0, 100))
    plt.ylim((0, 61))

    corr = df['subj_complexity'].corr(df['ResponseTime'], method='kendall')
    print('SubjComplexity ~ ResponseTime')
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['subj_complexity'], df['ResponseTime'])
    print('-> r squared:', r_value**2)

    plt.ylabel("Response Time in sec.")
    plt.xlabel("Subjective Complexity Rating")
        
    left, right = plt.xlim()
    ax1.text(left+((right-left)/40), 6, 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left+((right-left)/40), 1, 'r squared: ' + format(r_value**2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    plt.savefig(ROOT_DIR + '/analysis/output/SubjComplexity_ResponseTime.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(plt.gcf())


def plot_correlation_subjcomplexity_correctness(df):
    ax1 = df.plot(kind='scatter', x='subj_complexity', y='Correct', s=50, figsize=(7, 5))
    z = numpy.polyfit(df['subj_complexity'], df['Correct'], 1)
    p = numpy.poly1d(z)

    plt.plot(df['subj_complexity'], p(df['subj_complexity']), linewidth=1)
    plt.xlim((0, 100))
    plt.ylim((0, 100))

    corr = df['subj_complexity'].corr(df['Correct'], method='kendall')
    print('SubjComplexity ~ Correctness')
    print('-> Kendall corr:', corr)

    slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(df['subj_complexity'], df['Correct'])
    print('-> r squared:', r_value ** 2)

    plt.ylabel("Correct Responses in %")
    plt.xlabel("Subjective Complexity Rating")

    left, right = plt.xlim()
    ax1.text(left + ((right - left) / 40), 10, 'Kendall τ: ' + format(corr, '.2f'), fontdict=graph_label)
    ax1.text(left + ((right - left) / 40), 1, 'r squared: ' + format(r_value ** 2, '.2f'), fontdict=graph_label)

    sns.despine()
    plt.tight_layout()

    plt.savefig(ROOT_DIR + '/analysis/output/SubjComplexity_Correctness.pdf', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close(plt.gcf())


def select_color_for_metric(metric):
    if metric == "LOC":
        color = "#1f78b4"
    elif metric == "Halstead":
        color = "#33a02c"
    elif metric == "McCabe":
        color = "#ff7f00"
    else:
        color = "#6a3d9a"

    return color


def convert_to_second(time):
    return time / 1000


def convert_to_percent(percent):
    return percent * 100


def main():
    snippet_metrics = load_snippet_metrics()
    behavioral_data = load_behavioral_data()

    snippet_behavioral = pd.merge(snippet_metrics, behavioral_data, how='left', left_on=['Snippet'],
                                  right_on=['Snippet'])

    snippet_behavioral["ResponseTime"].fillna(60000, inplace=True)

    # check whether there is response times < 5s and possibly exclude them
    snippet_behavioral.loc[snippet_behavioral['ResponseTime'] < 5000, 'ResponseTime'] = numpy.nan
    snippet_behavioral = snippet_behavioral.dropna(subset=['ResponseTime'])

    snippet_behavioral["ResponseTime"] = snippet_behavioral['ResponseTime'].apply(convert_to_second)

    # compute correct correctness?
    snippet_correctness = snippet_behavioral.groupby('Snippet').mean()
    snippet_correctness["Correct"] = snippet_correctness['Correct'].apply(convert_to_percent)

    # create plots for metrics ~ response time & correctness
    metrics = ["LOC", "DepDegree", "McCabe", "Halstead"]  # for a small run with the four main representatives
    metrics = list(snippet_metrics)[2:]  # for a full run

    for metric in metrics:
        plot_correlation_responsetime(snippet_behavioral, metric)
        plot_correlation_correctness(snippet_correctness, metric)

    # correlate with behavioral data
    print('\n##### \n correlating subjective complexity with behavioral data')
    snippet_subjective_complexity = pd.read_csv(ROOT_DIR + '/data/subjective/SnippetSubjectiveComplexityRatings.csv')

    print('mean:' + str(snippet_subjective_complexity['subj_complexity'].mean()))
    print('std:' + str(snippet_subjective_complexity['subj_complexity'].std(ddof=1)))

    snippet_subj_complexity_behavioral_orig = pd.merge(snippet_subjective_complexity, snippet_behavioral, how='left',
                                                       left_on=['participant', 'snippet'],
                                                       right_on=['Participant', 'Snippet'])

    snippet_subj_complexity_behavioral = snippet_subj_complexity_behavioral_orig[
        ['participant', 'snippet', 'subj_complexity', 'Correct', 'ResponseTime']]

    # investigate why there are NaN values
    snippet_subj_complexity_behavioral.dropna(inplace=True)

    print(snippet_subj_complexity_behavioral.head(50))
    plot_correlation_subjcomplexity_responsetime(snippet_subj_complexity_behavioral)

    snippet_subj_complexity_behavioral_correctness = snippet_subj_complexity_behavioral.groupby('snippet').mean()
    snippet_subj_complexity_behavioral_correctness["Correct"] = snippet_subj_complexity_behavioral_correctness[
        'Correct'].apply(convert_to_percent)
    plot_correlation_subjcomplexity_correctness(snippet_subj_complexity_behavioral_correctness)

    # correlate with complexity metrics
    snippet_subj_complexity_metrics = snippet_subj_complexity_behavioral_orig[
        ['participant', 'snippet', 'subj_complexity', 'LOC', 'McCabe', 'Halstead', 'DepDegree']]
    snippet_subj_complexity_metrics.dropna(inplace=True)
    plot_correlation_subjcomplexity_metrics(snippet_subj_complexity_metrics, 'LOC')
    plot_correlation_subjcomplexity_metrics(snippet_subj_complexity_metrics, 'McCabe')
    plot_correlation_subjcomplexity_metrics(snippet_subj_complexity_metrics, 'Halstead')
    plot_correlation_subjcomplexity_metrics(snippet_subj_complexity_metrics, 'DepDegree')

    print('\n##### \n-> all done \o/')


if __name__ == "__main__":
    main()
