import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as offl


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
        positive = round(sum(list(state_date_1[states].values())), 2)
        negative = round(sum(list(state_date_neg_1[states].values())), 2)
        neutral = round(sum(list(state_date_0[states].values())), 2)
        total = positive + negative + neutral
        values_list.append(round(total, 2))

    for states in list(state_date_1.keys()):
        positive = round(sum(list(state_date_1[states].values())), 2)
        negative = round(sum(list(state_date_neg_1[states].values())), 2)
        neutral = round(sum(list(state_date_0[states].values())), 2)
        values_list.append(positive)
        values_list.append(negative)
        values_list.append(neutral)

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
        hovertemplate='<b>%{label} </b> <br> probability: %{value}',
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
        template='plotly_dark',
        xaxis=dict(
            showgrid=False
        ),
        yaxis=dict(
            showgrid=False
        ))

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))


def state_date_plot(state_date_positive, state_date_negative, state_date_neutral, state_name):
    '''For plotting different graphs of states with different dates and sentiments'''
    fig = go.Figure()

    fig.add_trace(go.Bar(x=list(state_date_positive.keys()),
                            y=list(state_date_positive.values()),
                            name='positive',
                            marker_color='rgb(0,128,0)'
                        ))
    fig.add_trace(go.Bar(x=list(state_date_negative.keys()),
                            y=list(state_date_negative.values()),
                            name='Negative',
                            marker_color='rgb(255,0,0)'
                        ))
    fig.add_trace(go.Bar(x=list(state_date_neutral.keys()),
                            y=list(state_date_neutral.values()),
                            name='Neutral',
                            marker_color='rgb(218,165,32)'
                        ))

    fig.update_layout(
        title={
            'text': f"Sentiment during lockdown of {state_name}",
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(
                    family='Rockwell',
                    color='dim gray',
                    size=30),
        },
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
        legend=dict(
            x=0.8,
            y=1.0,
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.2,
        bargroupgap=0.1,
        template='plotly_dark',
        updatemenus=[
            dict(
                buttons=list([
                    dict(
                        args=["type", "bar"],
                        label="Bar Graph",
                        method="restyle",
                    ),
                    dict(
                        args=[{"type": "scatter", "mode": 'lines+markers', "fill": None}],
                        label="Line Graph",
                        method="restyle"
                    ),
                    dict(
                        args=[
                            {"type": "scatter", "mode": 'markers+lines', "fill": 'tozeroy'}],
                        label="Area Plot",
                        method="restyle"
                    ),
                    dict(
                        args=[{"type": "scatter", "mode": 'markers', "fill": None}],
                        label="Scatter Plot",
                        method="update"
                    ),
                ]),
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.01,
                xanchor="left",
                y=1.2,
                yanchor="top",
                font = dict(color="rgb(220,20,60)")
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
                x=0.15,
                xanchor="left",
                y=1.2,
                yanchor="top",
                font=dict(color="rgb(220,20,60)")
            ),
        ])

    return(offl.plot(fig, show_link=False, output_type="div", include_plotlyjs=False))

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
            template='plotly_dark',
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

    fig.show()
    
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
    # Change the bar mode
    fig.update_layout(
        template='plotly_dark',
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

    fig.show()

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

    # Change the bar mode
    fig.update_layout(
            barmode='stack',
            template='plotly_dark',
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
                'text': f"Area plot",
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

    fig.show()

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

    # Change the bar mode
    fig.update_layout(
            template='plotly_dark',
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
                'text': f"markers plot",
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

    fig.show()