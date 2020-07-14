import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as offl
from plotly.subplots import make_subplots


class Plot():
    '''Used to plot different graphs by passing relevant arguments;
        requires main data points; In this particular case these are Dates and the sentiments like Positive, Negative, Neutral.
        Use them to plot different graphs and finding insights of the data;
        Particularly used for plotting different graphs between dates and sentiments'''

    def __init__(self, x_list, y_list):
        '''x_list : Takes in list objects of x axis for plotting different graphs(bar, line, etc) on the plotting area,
            y_list : Takes in list objects of y axis for plotting different graphs(bar, line, etc) on the plotting area.
            Example:-
                x_list = [x1, x2, x3,...], where x1, x2, x3 are further list objects for x axis that actualy have the data that goes on the plot,
                y_list = [y1, y2, y3,...], where y1, y2, y3 are further list objects for y axis that actualy have the data that goes on the plot.'''

        self.x_data = x_list
        self.y_data = y_list

    def trace_addition(self, graph_type, name=None, color=None):
        '''To update traces that are used for plotting.
            graph_type : enter graph type that you want to plot ex:-go.Line, go.Bar, etc.
            name : Names to be specified should be accordingly to data points that are parsed during the initialization of this class, list object.
            color : List object of different colors.'''
        self.trace_list = []

        for x_point, y_point, names, colors in zip(self.x_data, self.y_data, name, color):
            traces = graph_type(x=x_point,
                                y=y_point,
                                name=names,
                                marker_color=colors
                                )
            self.trace_list.append(traces)

    def plotting(self, title=None, x_title=None, y_title=None, x_range=None):
        '''plots the graph using plotly.
            title : Title of the plot.
            x_title : Title for x axis.
            y_title : Title for y axis.
            x_range : Passed to select particular range on x axis to show on plot.'''
        fig = go.Figure()

        for traces in self.trace_list:
            fig.add_trace(traces)

        fig.update_layout(
            title={
                'text': title,
                'y': 0.99,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                    family='Rockwell',
                    color='dim gray',
                    size=15),
            }, template='ggplot2',
            xaxis=dict(
                title=x_title,
                tickfont_size=14,
                tickangle=90,
                tickfont=dict(
                    family='Rockwell',
                    color='dim gray',
                    size=9),
                tickmode='linear',
                range=x_range,
            ),
            yaxis=dict(
                title=y_title,
                titlefont_size=16,
                tickfont_size=14,
            ),
            legend=dict(
                x=0.8,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.2,
            bargroupgap=0.1,
            plot_bgcolor='rgb(248,248,255)',
            
            # adding dropdown
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            label="Cummulative",
                            method="update",
                            args=[{"visible": [True, True, True]},
                                ]),
                        dict(
                            label="Positive",
                            method="update",
                            args=[{"visible": [True, False, False]},
                                ]),
                        dict(
                            label="Negative",
                            method="update",
                            args=[{"visible": [False, True, False]},
                                ]),
                        dict(
                            label="Neutral",
                            method="update",
                            args=[{"visible": [False, False, True]},
                                ]),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.01,
                    xanchor="left",
                    y=1.2,
                    yanchor="top"
                ),
            ]

        )
        return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


    def main_plot(self, graph_type, name=None, color=None, title=None,
                x_title=None, y_title=None, x_range=None):
        '''Plots the main graphs using plotly and to update traces that are used for plotting.
        title : Title of the plot.
        x_title : Title for x axis.
        y_title : Title for y axis.
        x_range : Passed to select particular range on x axis to show on plot.
        graph_type : enter graph type that you want to plot ex:-go.Line, go.Bar, etc.
        name : Names to be specified should be accordingly to data points that are parsed during the initialization of this class, list object.
        color : List object of different colors.'''
        fig = go.Figure()

        for x_point, y_point, names, colors in zip(self.x_data, self.y_data, name, color):
            traces = graph_type(x=x_point,
                                y=y_point,
                                name=names,
                                marker_color=colors
                                )
            fig.add_trace(traces)

        fig.update_layout(
            title={
                'text': title,
                'y': 0.99,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                    family='Rockwell',
                    color='dim gray',
                    size=30),
            },
            # to add dropdown
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            args=["type", "line"],
                            label="Line Graph",
                            method="restyle"
                        ),
                        dict(
                            args=["type", "bar"],
                            label="Bar Graph",
                            method="restyle"
                        ),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.01,
                    xanchor="left",
                    y=1.2,
                    yanchor="top"
                ),
                dict(
                    buttons=list([
                        dict(
                            label="Cummulative",
                            method="update",
                            args=[{"visible": [True, True, True]},
                            ]),
                        dict(
                            label="Positive",
                            method="update",
                            args=[{"visible": [True, False, False]},
                            ]),
                        dict(
                            label="Negative",
                            method="update",
                            args=[{"visible": [False, True, False]},
                            ]),
                        dict(
                            label="Neutral",
                            method="update",
                            args=[{"visible": [False, False, True]},
                            ]),
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.12,
                    xanchor="left",
                    y=1.2,
                    yanchor="top"
                ),
            ],
            xaxis=dict(
                title=x_title,
                tickfont_size=14,
                tickangle=90,
                tickfont=dict(
                    family='Rockwell',
                    color='dim gray',
                    size=9),
                tickmode='linear',
                range=x_range,
            ),
            yaxis=dict(
                title=y_title,
                titlefont_size=16,
                tickfont_size=14,
            ),
            legend=dict(
                x=0.85,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.2,
            bargroupgap=0.1,
            plot_bgcolor='rgb(248,248,255)',
        )

        return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))



    def donnut_pie(self, label, value, center_name=None, title=None):
        '''Returns pie chart according to parameters passed.
            label : List object for plotting labels on plot.
            value : List object of different values.
            center_name : Name to be shown on the center of pie chart(donut type).
            title : Title to be shown on the plot'''
        fig = go.Figure()
        coolors = ['rgb(42, 199, 78)', 'rgb(232, 14, 14)', 'rgb(232, 228, 12)']
        fig.add_trace(go.Pie(labels=label, values=value),
                        )

        fig.update_traces(hole=.4, hoverinfo="label+percent+value", marker=dict(colors=coolors, line=dict(color='#000000', width=1)))

        fig.update_layout(
            title_text=title,
            annotations=[dict(text=center_name, x=0.5, y=0.5, font_size=20, showarrow=False),
                            ])
        return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


def sunburst_chart(state_date_1, state_date_neg_1, state_date_0):
    '''This function plots states with its cummulative positive, negative, and neutral probabilities in form of sunburst chart'''

    # Creating values list for sunburst plot
    values_list = []
    
    for states in list(state_date_1.keys()):
        positive = state_date_1[states]
        negative = state_date_neg_1[states]
        neutral = state_date_0[states]
        total = positive + negative + neutral
        values_list.append(total)

    for states in list(state_date_1.keys()):
        values_list.append(state_date_1[states])
        values_list.append(state_date_neg_1[states])
        values_list.append(state_date_0[states])

    # Creating labels for sunburst plot
    labels_list = list(state_date_1.keys())
    for states in list(state_date_1.keys()):
        labels_list.append(f"Positive in {states}")
        labels_list.append(f"Negative in {states}")
        labels_list.append(f"Neutral in {states}")

    # Creating parent list for sunburst plot
    parent_list = [""]*33+sorted(list(state_date_1.keys())*3)

    fig = go.Figure()

    fig = go.Figure(go.Sunburst(
        labels=labels_list,
        parents=parent_list,
        values=values_list,
        maxdepth=2,
        branchvalues='total',
        hovertemplate='<b>%{label} </b> <br> sentiment percentage: %{value}',
        name=''
    ))

    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


def box_plot(y_positive, y_negative, y_neutral, name):
    '''plot box plot takes in list of y variables that we want to plot'''
    fig = go.Figure()
    fig.add_trace(go.Box(y=y_positive,
                        name='positive'
                            ))
    fig.add_trace(go.Box(y=y_negative,
                        name='Negative'
                            ))
    fig.add_trace(go.Box(y=y_neutral,
                        name='Neutral'
                            ))

    fig.update_layout(
        title={
            'text': f"BoxPlot of sentiments of {name}",
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                    family='Rockwell',
                    color='dim gray',
                    size=30),
        },
        #template='plotly_dark',
        xaxis=dict(
            showgrid=False
        ),
        yaxis=dict(
            showgrid=False
        ))

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


def state_date_plot(state_date_positive, state_date_negative, state_date_neutral, state_name):
    '''For plotting different graphs of states with different dates and sentiments'''
    fig = make_subplots(rows=3,
                        cols=1,
                        shared_xaxes=True,
                        )

    fig.add_trace(go.Scatter(x=list(state_date_positive.keys()),
                             y=list(state_date_positive.values()),
                             name='positive😊',
                             mode='lines+markers',
                             marker_color='rgb(0,128,0)',
                             fillcolor='yellow'
                             ), row=1, col=1)
    fig.add_trace(go.Scatter(x=list(state_date_negative.keys()),
                             y=list(state_date_negative.values()),
                             name='Negative🙁',
                             mode='lines+markers',
                             marker_color='rgb(255,0,0)'
                             ), row=2, col=1)
    fig.add_trace(go.Scatter(x=list(state_date_neutral.keys()),
                             y=list(state_date_neutral.values()),
                             name='Neutral😑',
                             mode='lines+markers',
                             marker_color='rgb(218,165,32)'
                             ), row=3, col=1)

    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')

    # Updating x_axis properties
    fig.update_xaxes(
        showline=True,
        linewidth=2,
        linecolor='darkgreen',
        row=1, col=1)

    fig.update_xaxes(
        showline=True,
        linewidth=2,
        linecolor='darkred',
        row=2, col=1)

    fig.update_xaxes(
        showline=True,
        linewidth=2,
        linecolor='goldenrod',
        row=3, col=1)

    # Updating y_axis properties
    fig.update_yaxes(title='Sentiments',
                     titlefont_size=16,
                     showline=True,
                     linewidth=2,
                     linecolor='darkgreen',
                     row=1, col=1)

    fig.update_yaxes(title='Sentiments',
                     titlefont_size=16,
                     showline=True,
                     linewidth=2,
                     linecolor='darkred',
                     row=2, col=1)

    fig.update_yaxes(title='Sentiments',
                     titlefont_size=16,
                     showline=True,
                     linewidth=2,
                     linecolor='goldenrod',
                     row=3, col=1)

    # Updating shapes
    fig.update_layout(
        shapes=[
            dict(
                type='rect',
                xref='paper',
                yref="y",
                x0=0,
                y0=-0.1,
                x1=1,
                y1=1.1,
                fillcolor='green',
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            dict(
                type='rect',
                xref='paper',
                yref="y2",
                x0=0,
                y0=-0.1,
                x1=1,
                y1=1.1,
                fillcolor='red',
                opacity=0.4,
                layer="below",
                line_width=0,
            ),
            dict(
                type='rect',
                xref='paper',
                yref="y3",
                x0=0,
                y0=-0.1,
                x1=1,
                y1=1.1,
                fillcolor='gold',
                opacity=0.4,
                layer="below",
                line_width=0,
            )
        ]
    )

    fig.update_layout(
        width=600,
        height=800,
        bargap=0.2,
        bargroupgap=0.1,

        # adding dropdown
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"type": "line"}],
                        label="Cummulative",
                        method="restyle"
                    ),
                    dict(
                        args=[{"type": "bar"}],
                        label="Daily",
                        method="restyle"
                    ),
                ]),
                type='buttons',
                direction="right",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.01,
                xanchor="left",
                y=1.1,
                yanchor="top",
                font=dict(color="black")
            ),
        ]
    )

    config = {'displayModeBar': True,
              'responsive': False,
              'modeBarButtonsToRemove': ['toggleSpikelines',
                                         'hoverCompareCartesian',
                                         'zoom2d',
                                         'pan2d',
                                         'select2d',
                                         'lasso2d'],
              'displaylogo': False
              }

    return(offl.plot(fig, show_link=False, output_type="div",
                        include_plotlyjs=False, config=config))


def stacked_barplot(x_list, y_list):
    '''Plot stacked barplot'''
    
    for x_labels, y_labels in zip(x_list, y_list):
        fig = go.Figure(data=[
        go.Bar(name='Positive', x=x_labels, y=y_labels,
                marker_color='green',
                marker_line_color='darkgreen'
                ),
        go.Bar(name='Negative', x=x_labels, y=y_labels,
                marker_color='red',
                marker_line_color='darkred'
                ),
        go.Bar(name='Neutral', x=x_labels, y=y_labels,
                marker_color='yellow',
                marker_line_color='gold'
                )
                ])
    
    fig.update_traces(marker_line_width=1, opacity=0.7)
    
    # Change the layout
    fig.update_layout(
            barmode='stack',
            #template='plotly_dark',
            xaxis=dict(
                title='Dates',
                tickfont_size=14,
                tickangle=90,
                tickfont=dict(
                    family='Rockwell',
                    color='dim gray',
                    size=9),
                tickmode='linear',
                showgrid=False
                ),
            yaxis=dict(
                title='Sentiments',
                titlefont_size=16,
                tickfont_size=14,
                showgrid=False
                ),
            bargap=0.3,
            title={
                'text': "stacked barplot",
                'y':0.99,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                        family='Rockwell',
                        color='dim gray',
                        size=30),
                },
            updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                label="Cummulative",
                                method="update",
                                args=[{"visible": [True, True, True]},
                                        ]),
                            dict(
                                label="Positive",
                                method="update",
                                args=[{"visible": [True, False, False]},
                                        ]),
                            dict(
                                label="Negative",
                                method="update",
                                args=[{"visible": [False, True, False]},
                                        ]),
                            dict(
                                label="Neutral",
                                method="update",
                                args=[{"visible": [False, False, True]},
                                        ]),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.01,
                        xanchor="left",
                        y=1.2,
                        yanchor="top",
                        font=dict(color="rgb(220,20,60)")
                    ),
                ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))
    
def barplot(x_list, y_list):
    '''plots the barplot'''
    
    for x_labels, y_labels in zip(x_list, y_list):
        fig = go.Figure(data=[
            go.Bar(name='Positive', x=x_labels, y=y_labels,
                    marker_color='green',
                    marker_line_color='darkgreen'
                    ),
            go.Bar(name='Negative', x=x_labels, y=y_labels,
                    marker_color='red',
                    marker_line_color='red'
                    ),
            go.Bar(name='Neutral', x=x_labels, y=y_labels,
                    marker_color='yellow',
                    marker_line_color='gold'
                    )
                ])


    fig.update_traces(marker_line_width=0.5, opacity=1)
    # Change the layout of out
    fig.update_layout(
        #template='plotly_dark',
        xaxis=dict(
            title='Dates',
            tickfont_size=14,
            tickangle=90,
            tickfont=dict(
                family='Rockwell',
                color='dim gray',
                size=9),
            tickmode='linear',
            showgrid=False
        ),
        yaxis=dict(
            title='Sentiments',
            titlefont_size=16,
            tickfont_size=14,
            showgrid=False
        ),
        bargap=0.3,
        bargroupgap=0.2,
        title={
            'text': "Barplot",
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                family='Rockwell',
                color='dim gray',
                size=30),
        },
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        label="Cummulative",
                        method="update",
                        args=[{"visible": [True, True, True]},
                            ]),
                    dict(
                        label="Positive",
                        method="update",
                        args=[{"visible": [True, False, False]},
                            ]),
                    dict(
                        label="Negative",
                        method="update",
                        args=[{"visible": [False, True, False]},
                            ]),
                    dict(
                        label="Neutral",
                        method="update",
                        args=[{"visible": [False, False, True]},
                            ]),
                ]),
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.01,
                xanchor="left",
                y=1.2,
                yanchor="top",
                font=dict(color="rgb(220,20,60)")
            ),
        ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))

def area_plot(x_list, y_list):
    '''plots the area plot'''
    
    fig = go.Figure()

    for x_labels, y_labels in zip(x_list, y_list):
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='lines+markers',
                        name='positive',
                        marker_color='green',
                        marker_line_color='darkgreen',
                        fill='tozeroy'
                        ))
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='lines+markers',
                        name='Negative',
                        marker_color='red',
                        marker_line_color='red',
                        fill='tozeroy'
                        ))
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='lines+markers',
                        name='Neutral',
                        marker_color='gold',
                        marker_line_color='gold',
                        fill='tozeroy'
                        ))

    fig.update_traces(marker_line_width=1.5, opacity=0.7)

    # Change the layout of the plot
    fig.update_layout(
            barmode='stack',
            #template='plotly_dark',
            xaxis=dict(
                title='Dates',
                tickfont_size=14,
                tickangle=90,
                tickfont=dict(
                    family='Rockwell',
                    color='dim gray',
                    size=9),
                tickmode='linear',
                showgrid=False
                ),
            yaxis=dict(
                title='Sentiments',
                titlefont_size=16,
                tickfont_size=14,
                showgrid=False
                ),
            bargap=0.3,
            title={
                'text': "Area plot",
                'y':0.99,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                        family='Rockwell',
                        color='dim gray',
                        size=30),
                },
            updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                label="Cummulative",
                                method="update",
                                args=[{"visible": [True, True, True]},
                                        ]),
                            dict(
                                label="Positive",
                                method="update",
                                args=[{"visible": [True, False, False]},
                                        ]),
                            dict(
                                label="Negative",
                                method="update",
                                args=[{"visible": [False, True, False]},
                                        ]),
                            dict(
                                label="Neutral",
                                method="update",
                                args=[{"visible": [False, False, True]},
                                        ]),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.01,
                        xanchor="left",
                        y=1.2,
                        yanchor="top",
                        font=dict(color="rgb(220,20,60)")
                    ),
                ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))

def scatter_plot(x_list, y_list):
    '''plots the scatter plot'''
    
    fig = go.Figure()

    for x_labels, y_labels in zip(x_list, y_list):
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='markers',
                        name='positive',
                        marker_color='lightgreen',
                        marker_line_color='green',
                        marker_size=20
                        ))
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='markers',
                        name='Negative',
                        marker_color='orange',
                        marker_line_color='red',
                        marker_size=20
                        ))
        fig.add_trace(go.Scatter(x=x_labels,
                        y=y_labels,
                        mode='markers',
                        name='Neutral',
                        marker_color='yellow',
                        marker_line_color='gold',
                        marker_size=20
                        ))

    fig.update_traces(marker_line_width=1.5, opacity=1)

    # Change the layout of the plot
    fig.update_layout(
            #template='plotly_dark',
            xaxis=dict(
                title='Dates',
                tickfont_size=14,
                tickangle=90,
                tickfont=dict(
                    family='Rockwell',
                    color='dim gray',
                    size=9),
                tickmode='linear',
                showgrid=False
                ),
            yaxis=dict(
                title='Sentiments',
                titlefont_size=16,
                tickfont_size=14,
                showgrid=False
                ),
            bargap=0.3,
            title={
                'text': "markers plot",
                'y':0.99,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                        family='Rockwell',
                        color='dim gray',
                        size=30),
                },
            updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                label="Cummulative",
                                method="update",
                                args=[{"visible": [True, True, True]},
                                        ]),
                            dict(
                                label="Positive",
                                method="update",
                                args=[{"visible": [True, False, False]},
                                        ]),
                            dict(
                                label="Negative",
                                method="update",
                                args=[{"visible": [False, True, False]},
                                        ]),
                            dict(
                                label="Neutral",
                                method="update",
                                args=[{"visible": [False, False, True]},
                                        ]),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.01,
                        xanchor="left",
                        y=1.2,
                        yanchor="top",
                        font=dict(color="rgb(220,20,60)")
                    ),
                ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))

def line_plot(x_list, y_list):
    '''plots the line plot'''
    
    fig = go.Figure()

    for x_labels, y_labels in zip(x_list, y_list):
        fig.add_trace(go.Scatter(x=x_labels,
                                y=y_labels,
                                mode='lines+markers',
                                name='positive',
                                marker_color='lightgreen',
                                marker_line_color='green'
                                ))
        fig.add_trace(go.Scatter(x=x_labels,
                                y=y_labels,
                                mode='lines+markers',
                                name='Negative',
                                marker_color='orange',
                                marker_line_color='red'
                                ))
        fig.add_trace(go.Scatter(x=x_labels,
                                y=y_labels,
                                mode='lines+markers',
                                name='Neutral',
                                marker_color='yellow',
                                marker_line_color='gold'
                                ))

    fig.update_traces(marker_line_width=1.5, opacity=1)

    # Change the plot layout
    fig.update_layout(
        barmode='stack',
        #template='plotly_dark',
        xaxis=dict(
            title='Dates',
            tickfont_size=14,
            tickangle=90,
            tickfont=dict(
                family='Rockwell',
                color='dim gray',
                size=9),
            tickmode='linear',
            showgrid=False
        ),
        yaxis=dict(
            title='Sentiments',
            titlefont_size=16,
            tickfont_size=14,
            showgrid=False
        ),
        bargap=0.3,
        title={
            'text': "lines+markers plot",
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                family='Rockwell',
                color='dim gray',
                size=30),
        },
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        label="Cummulative",
                        method="update",
                        args=[{"visible": [True, True, True]},
                            ]),
                    dict(
                        label="Positive",
                        method="update",
                        args=[{"visible": [True, False, False]},
                            ]),
                    dict(
                        label="Negative",
                        method="update",
                        args=[{"visible": [False, True, False]},
                            ]),
                    dict(
                        label="Neutral",
                        method="update",
                        args=[{"visible": [False, False, True]},
                            ]),
                ]),
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.01,
                xanchor="left",
                y=1.2,
                yanchor="top",
                font=dict(color="rgb(220,20,60)")
            ),
        ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))

def violin_plot(y_list):
    '''plots violin plot'''
    
    fig = go.Figure()
    for y_labels in y_list:
        fig.add_trace(go.Violin(y=y_labels,
                        box_visible=True, line_color='green',
                        meanline_visible=True,
                        fillcolor='lightgreen', opacity=0.6,
                        x0='Positive', name='Positive')
            )
        fig.add_trace(go.Violin(y=y_labels,
                        box_visible=True, line_color='red',
                        meanline_visible=True,
                        fillcolor='orange', opacity=0.6,
                        x0='Negative', name='Negative')
            )
        fig.add_trace(go.Violin(y=y_labels,
                        box_visible=True, line_color='yellow',
                        meanline_visible=True,
                        fillcolor='lightyellow', opacity=0.6,
                        x0='Neutral', name='Neutral')
            )

    fig.update_traces(box_visible=True, meanline_visible=True)
    
    # Change the plot layout
    fig.update_layout(
        violinmode='group',
        yaxis_zeroline=False,
            #template='plotly_dark',
            yaxis=dict(
                title='Sentiments',
                titlefont_size=16,
                tickfont_size=14,
                showgrid=False
                ),
            bargap=0.3,
            title={
                'text': "violin plot",
                'y':0.99,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(
                        family='Rockwell',
                        color='dim gray',
                        size=30),
                },
            updatemenus=[
                    dict(
                        buttons=list([
                            dict(
                                label="Cummulative",
                                method="update",
                                args=[{"visible": [True, True, True]},
                                        ]),
                            dict(
                                label="Positive",
                                method="update",
                                args=[{"visible": [True, False, False]},
                                        ]),
                            dict(
                                label="Negative",
                                method="update",
                                args=[{"visible": [False, True, False]},
                                        ]),
                            dict(
                                label="Neutral",
                                method="update",
                                args=[{"visible": [False, False, True]},
                                        ]),
                        ]),
                        direction="down",
                        pad={"r": 10, "t": 10},
                        showactive=True,
                        x=0.01,
                        xanchor="left",
                        y=1.2,
                        yanchor="top",
                        font=dict(color="rgb(220,20,60)")
                    ),
                ]
    )
    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


def phases_plot(x_list, y_list, name):
    '''name takes one of these values: ["phase 1", "phase 2", "phase 3", "phase 4"].
        x_list is the list of x_labels.
        y_list is the list of y_labels'''
    x_layout_list = []
    x_labels_list = []
    y_labels_list = []

    for x_labels, y_labels in zip(x_list, y_list):
        if name == 'phase 1':
            x_layout_list.append(x_labels[4:25])
            x_labels_list.append(x_labels[5:24])
            y_labels_list.append(y_labels[5:24])
        elif name == 'phase 2':
            x_layout_list.append(x_labels[23:44])
            x_labels_list.append(x_labels[24:43])
            y_labels_list.append(y_labels[24:43])
        elif name == 'phase 3':
            x_layout_list.append(x_labels[42:57])
            x_labels_list.append(x_labels[43:56])
            y_labels_list.append(y_labels[43:56])
        elif name == 'phase 4':
            x_layout_list.append(x_labels[55:71])
            x_labels_list.append(x_labels[56:70])
            y_labels_list.append(y_labels[56:70])

    names_list = ['Positive😊', 'Negative🙁', 'Neutral😐']
    color_list = ['green', 'red', 'gold']
    x_refer_list = ['x', 'x2', 'x3']
    col_list = [1, 2, 3]

    fig = make_subplots(rows=1,
                        cols=3,
                        shared_yaxes=True,
                        )

    for names, cols, colors, x_labels, y_labels in zip(names_list, col_list, color_list,
                                                        x_labels_list, y_labels_list):
        fig.add_trace(go.Scatter(x=x_labels,
                                y=y_labels,
                                mode="lines+markers",
                                name=names,
                                marker_color=colors), row=1, col=cols)

    for cols in col_list:
        # Update xaxis properties
        fig.update_xaxes(showgrid=False, row=1, col=cols)

        # Update yaxis properties
        if cols == 1:
            fig.update_yaxes(title='Sentiments',
                            titlefont_size=16,
                            zeroline=False,
                            row=1, col=cols)
        else:
            fig.update_yaxes(titlefont_size=16,
                            zeroline=False,
                            row=1, col=cols)

    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')

    shapes_list = []
    # Update plot color
    for colors, x_labels, x_refers in zip(color_list, x_layout_list, x_refer_list):
        shape_dict = dict(
            type="rect",
            xref=x_refers,
            yref="paper",
            x0=x_labels[0],
            y0=0,
            x1=x_labels[-1],
            y1=1,
            fillcolor=colors,
            opacity=0.4,
            layer="below",
            line_width=0,
        )
        shapes_list.append(shape_dict)

    # Updating dropdown and theme
    fig.update_layout(
        shapes=shapes_list,
        height=400,
        bargap=0.2,
        bargroupgap=0.1,

        # adding dropdown
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=[{"type": "line"}],
                        label="Cummulative",
                        method="restyle"
                    ),
                    dict(
                        args=[{"type": "bar"}],
                        label="Daily",
                        method="restyle"
                    ),
                ]),
                type='buttons',
                direction="right",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.01,
                xanchor="left",
                y=1.4,
                yanchor="top",
                font=dict(color="black")
            ),
        ]

    )

    config = {'displayModeBar': True,
                'responsive': False,
                'modeBarButtonsToRemove': ['toggleSpikelines',
                                        'hoverCompareCartesian',
                                        'zoom2d',
                                        'pan2d',
                                        'select2d',
                                        'lasso2d'],
                'displaylogo': False
            }
    return(offl.plot(fig, show_link=False, output_type="div",
                    include_plotlyjs=False, config=config))


def tags_barplot(state_tags_dict, state_name):

    ## Color list to filled in bars
    colors = ['#bcbddc', '#9e9ac8', '#807dba', '#6a51a3', '#54278f']

    ## Main plot
    # create figure
    fig = go.Figure()

    # Use textposition='auto' for direct text
    fig = go.Figure(data=[go.Bar(
        x=list(state_tags_dict[state_name].keys()),
        y=list(state_tags_dict[state_name].values()),
        text=list(state_tags_dict[state_name].values()),
        textposition='outside',
    )])

    # Customize aspect
    fig.update_traces(marker_color=colors[::-1], marker_line_color='black',
                      marker_line_width=1.5, opacity=0.6, hoverinfo="none")

    # Updating x-axis properties
    fig.update_xaxes(showgrid=False, showticklabels=False)

    # Updating y-axis properties
    fig.update_yaxes(showgrid=False, showticklabels=False, automargin=True)

    # Updating layout
    fig.update_layout(template='plotly_white',
                      width=450,
                      height=450
                      )

    config = {'staticPlot': True, 'responsive': False}
    return(offl.plot(fig, show_link=False, output_type="div",
                        include_plotlyjs=False, config=config)
            )

def predict_plots(date, output_data, train_data, valid_data):    
    ## Creating data for train part
    train_data_pos = list(train_data['train_pos'])
    train_data_neg = list(train_data['train_neg'])
    train_data_neut = list(train_data['train_neut'])
    
    ## Creating data for valid part
    valid_data_pos = list(valid_data['valid_pos'])
    valid_data_pred_pos = list(valid_data['valid_pos_pred'])
    valid_data_neg = list(valid_data['valid_neg'])
    valid_data_pred_neg = list(valid_data['valid_neg_pred'])
    valid_data_neut = list(valid_data['valid_neut'])
    valid_data_pred_neut = list(valid_data['valid_neut_pred'])
    
    ## Creating data for next 7 days pred
    lst_output_pos = list(output_data['lst_output_pos'])
    lst_output_neg = list(output_data['lst_output_neg'])
    lst_output_neut = list(output_data['lst_output_neut'])
    lst_output_pos.append('')
    lst_output_neg.append('')
    lst_output_neut.append('')
    
    # The date list for x labels
    the_dates = ['2020-06-01', '2020-06-02', '2020-06-03',
                '2020-06-04', '2020-06-05', '2020-06-06',
                '2020-06-07', '2020-06-08'
                ]

    ## Initialized subplot graphs
    fig = make_subplots(rows=1,
                        cols=3,
                        shared_yaxes=True,
                        subplot_titles=("Positive😊", "Negative🙁", "Neutral😑")
                        )

    # Trace for positive graph
    fig.add_trace(
        go.Scatter(
            x=list(date)[40:56],
            y=train_data_pos,
            mode='lines',
            name='Training',
            line = dict(width=2.5, color='skyblue')
        ), row=1, col=1)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_pos,
            mode='lines',
            name='Validation',
            line = dict(width=2.5, color='red')
        ), row=1, col=1)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_pred_pos,
            mode='lines',
            name='Predictions',
            line = dict(width=2.5, color='green')
        ), row=1, col=1)
    fig.add_trace(
        go.Scatter(
            x=the_dates,
            y=lst_output_pos,
            mode='lines',
            name='Next 7 Days',
            line = dict(width=2.5, color='purple')
        ), row=1, col=1)

    # Trace for negative graphs
    fig.add_trace(
        go.Scatter(
            x=list(date)[40:57],
            y=train_data_neg,
            mode='lines',
            line = dict(width=2.5, color='skyblue'),
            showlegend=False,
            name='Training',
        ), row=1, col=2)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_neg,
            mode='lines',
            line = dict(width=2.5, color='red'),
            showlegend=False,
            name='Validation',
        ), row=1, col=2)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_pred_neg,
            mode='lines',
            line = dict(width=2.5, color='green'),
            showlegend=False,
            name='Predictions',
        ), row=1, col=2)
    fig.add_trace(
        go.Scatter(
            x=the_dates,
            y=lst_output_neg,
            mode='lines',
            line = dict(width=2.5, color='purple'),
            showlegend=False,
            name='Next 7 days',
        ), row=1, col=2)

    # Trace for neutral graph
    fig.add_trace(
        go.Scatter(
            x=list(date)[40:56],
            y=train_data_neut,
            mode='lines',
            line = dict(width=2.5, color='skyblue'),
            showlegend=False,
            name='Training',
        ), row=1, col=3)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_neut,
            mode='lines',
            line = dict(width=2.5, color='red'),
            showlegend=False,
            name='Validation',
        ), row=1, col=3)
    fig.add_trace(
        go.Scatter(
            x=list(date)[56:],
            y=valid_data_pred_neut,
            mode='lines',
            line = dict(width=2.5, color='green'),
            showlegend=False,
            name='Predictions',
        ), row=1, col=3)
    fig.add_trace(
        go.Scatter(
            x=the_dates,
            y=lst_output_neut,
            mode='lines',
            line = dict(width=2.5, color='purple'),
            showlegend=False,
            name='Next 7 days',
        ), row=1, col=3)

    # Update xaxis properties
    fig.update_xaxes(ticks="outside",
                    tickwidth=2,
                    tickcolor='crimson',
                    ticklen=10,
                    showline=True,
                    linewidth=2,
                    linecolor='black')

    # Update yaxis properties
    fig.update_yaxes(title='Sentiments',
                    titlefont_size=16,
                    zeroline=False,
                    ticks="outside",
                    tickwidth=2,
                    tickcolor='crimson',
                    ticklen=10,
                    showline=True,
                    linewidth=2,
                    linecolor='black',
                    row=1, col=1)

    # Updating layout
    fig.update_layout(
        height=400,
        width=1200,
    )

    ## Added extra configuration to the plot
    config = {'displayModeBar': True,
                'responsive': False,
                'modeBarButtonsToRemove': ['toggleSpikelines',
                                        'hoverCompareCartesian',
                                        'zoom2d',
                                        'pan2d',
                                        'select2d',
                                        'lasso2d'],
                'displaylogo': False
            }
    return(offl.plot(fig, show_link=False, output_type="div",
                        include_plotlyjs=False, config=config)
            )