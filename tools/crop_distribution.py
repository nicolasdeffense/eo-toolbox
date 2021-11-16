#!/usr/bin/python3

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from matplotlib.patches import Patch
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots


# ------------------------------------------------------------------------------------------------

def prepare_dataframe(gdf, lut, level,  area_column='area'):

    level_nb = level + '_nb'

    lut_df = pd.read_excel(lut)

    gdf_lut = gdf.merge(lut_df, left_on='sub_nb', right_on='sub_nb', how='inner')

    df_area = gdf_lut.groupby(level_nb)[area_column].agg('sum').reset_index(name='area_tot')

    df_area['area_tot'] = (df_area['area_tot']/10000).round(2)

    df_count = gdf_lut.groupby(level_nb).size().reset_index(name='count')

    df = df_area.merge(df_count, on=level_nb)
    
    lut_df = lut_df.drop_duplicates(level_nb)
    
    df = df.merge(lut_df, on=level_nb)

    df = df.sort_values(by='area_tot', ascending=False)

    df['ratio'] = ((df['area_tot'] / df['area_tot'].sum())*100).round(2)
    
    df['cumsum'] = df['area_tot'].cumsum()
    df['cumsum_ratio'] = ((df['cumsum'] / df['cumsum'].iloc[-1])*100).round(2)

    df.loc[df['lc_nb']==1,'color'] = '#ffff64'
    df.loc[df['lc_nb']==2,'color'] = '#c8c864'
    df.loc[df['lc_nb']==3,'color'] = '#ffb432'
    df.loc[df['lc_nb']==4,'color'] = '#ffebaf'
    df.loc[df['lc_nb']==5,'color'] = '#966400'
    df.loc[df['lc_nb']==6,'color'] = '#00a000'
    df.loc[df['lc_nb']==7,'color'] = '#fff5d7'
    df.loc[df['lc_nb']==8,'color'] = '#c31400'
    df.loc[df['lc_nb']==9,'color'] = '#0046c8'

    df[level] = df[level].str.slice(start=0, stop=20)

    # --------- #
    # Get table #
    # --------- #

    #prop_df = df[['sub_nb','sub','lc_nb','lc','cumsum_ratio']]
    #print(prop_df)
    #print('-- Creating table')
    #print(f'----> {prop_csv}')
    #prop_df.to_csv(prop_csv, index=False, sep=';')

    return df

# ------------------------------------------------------------------------------------------------

def pie_chart_plotly(df, chart_filename, level, values='area_tot'):

    if level == 'lc':

        color_dict = {}

        for i, row in df.iterrows():
            lc    = row['lc']
            color = row['color']
            color_dict[lc] = color

        fig = px.pie(df,
                    values='area_tot',
                    names=level,
                    color='lc',
                    color_discrete_map=color_dict,
                    hover_data=['count']
                    )
    
    else:
        fig = px.pie(df,
                    values='area_tot',
                    names=level,
                    color=level,
                    hover_data=['count']
                    )

    fig.show()

    fig.write_html(chart_filename + '.html')
    fig.write_image(chart_filename + '.svg')


# ------------------------------------------------------------------------------------------------

def bar_chart_plotly(df, chart_filename, level, y='ratio'):

    
    if level == 'lc':

        color_dict = {}

        for i, row in df.iterrows():
            lc    = row['lc']
            color = row['color']
            color_dict[lc] = color

        fig = px.bar(df,
                x=level,
                y=y,
                color='lc',
                color_discrete_map=color_dict,
                hover_data=["area_tot", "count","ratio"],
                text='count')
    
    else:
        fig = px.bar(df,
                x=level,
                y=y,
                color=level,
                hover_data=["area_tot", "count","ratio"],
                text='count')

    fig.show()

    fig.write_html(chart_filename + '.html')
    fig.write_image(chart_filename + '.svg')


# ------------------------------------------------------------------------------------------------

def grouped_bar_chart_plotly(df_1, df_2, plotly_html, level, y='ratio'):

    df_list = [df_1, df_2]

    df = pd.concat(df_list)

    display(df)

    fig = px.bar(df,
            x=level,
            y=y,
            text='count',
            color='name',
            barmode='group',
            hover_data=["area", "count","ratio"])

    fig.show()

    fig.write_html(plotly_html)

# ------------------------------------------------------------------------------------------------

def build_histogram_matplotlib(df, histo_png, level, area_column='area', distribution='area', cumsum=True, display_legend=False):

    width = 0.55
    stop = 20
    x_size = 10
    
    #plt.figure(figsize = (15, 10))
    fig, ax = plt.subplots(figsize = (15, 10))

    if distribution == 'area':
        plt.bar(df[level].str.slice(start=0, stop=stop), df['area'], width, color=df['color'])
        plt.ylabel('Area [m2]', size=12)

    elif distribution == 'count':
        plt.bar(df[level].str.slice(start=0, stop=stop), df['count'], width, color=df['color'])
        plt.ylabel('Number of polygons', size=12)
    

    plt.xticks(rotation=90)
    plt.tick_params(axis='x', labelsize=x_size)
    plt.tick_params(axis='y',labelsize=10)

    if display_legend:
        legend_elements = [Patch(facecolor='#ffff64',label='Annual cropland'),
                            Patch(facecolor='#c8c864',label='Perennial crops'),
                            Patch(facecolor='#ffb432',label='Grassland and meadows'),
                            Patch(facecolor='#ffebaf',label='Fallows'),
                            Patch(facecolor='#966400',label='Shrub land'),
                            Patch(facecolor='#00a000',label='Forest'),
                            Patch(facecolor='#fff5d7',label='Bare soil'),
                            Patch(facecolor='#c31400',label='Build-up surface'),
                            Patch(facecolor='#0046c8',label='Water bodies')]

        plt.legend(handles=legend_elements, fontsize='x-small', loc='upper right', bbox_to_anchor=(1, 0.9))
    

    if cumsum:
        plt.twinx()
        plt.plot(df[level].str.slice(start=0, stop=stop), df['cumsum_ratio'])
        plt.axhline(y=0.95, linewidth=1, color='r', linestyle='--')
        plt.ylabel('Cumulative sum', size=12)
        plt.tick_params(axis='y',labelsize=10)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    
    plt.tight_layout()

    #plt.show()
    
    print('-- Creating histogram')
    print(f'----> {histo_png}')

    plt.savefig(histo_png, bbox_inches='tight', dpi=300)


# ------------------------------------------------------------------------------------------------

def get_proportion_lc(df, pie_png, level, area_column='area', distribution='area'):
        
    df['explode'] = 0.01
    
    plt.figure(dpi=1200)

    plt.tight_layout()

    #plt.pie(df['area'], labels=df[level], colors=df['color'], autopct='%1.2f%%', explode=df['explode'], pctdistance=0.9, labeldistance=1.05, textprops={'fontsize': 5})

    plt.pie(df['area'], labels=df[level], autopct='%1.2f%%', explode=df['explode'], pctdistance=0.9, labeldistance=1.05, textprops={'fontsize': 5})

    plt.savefig(pie_png, bbox_inches='tight')