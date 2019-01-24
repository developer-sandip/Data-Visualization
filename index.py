import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

import numpy as np
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

app = dash.Dash()

app.layout= html.Div([
            dcc.Dropdown(

                        id= 'my-dropdown',
                        options=[
                        {'label': 'By Purpose','value': 'BP'},
                        {'label': 'By Gender','value': 'BG'},
                        {'label': 'By Month','value': 'BM'},
                        {'label': 'By number of Trekkers','value': 'BNT'}
                        ],
                        value = 'BM')
                        ,
                        
            dcc.Graph(id='scatterplot',
                    figure= { 'data'  : [go.Scatter(x=x_values, y=y_values+5, mode='lines+markers', name='LM')],
                              'layout': go.Layout(title='Tourist arrival by month from 1992-2013',
                                                  xaxis= {'title': 'Months'},
                                                  yaxis= {'title': 'No of Tourist'})
                        })
])


#@app.callback(Output('scatterplot', 'figure'),[Input('my-dropdown', 'value'])
#def update_figure(selected_option):
    #return


if __name__ == '__main__':
    app.run_server()
