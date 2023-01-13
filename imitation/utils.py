import plotly.express
from plotly.graph_objects import (
	Figure,
	Pie
)
from imitation.models import Incident

def get_main_chart():
	incident_list = Incident.objects.all().order_by('created_at')
	if not incident_list:
		return False
	y_list,x_list = list(), list()
	for index,incident in enumerate(incident_list):
	    y_list.append(index+1)
	    x_list.append(incident.created_at)
	chart_data = plotly.express.line(x=list(reversed(x_list)),
									 y=list(reversed(y_list)),
									 title="График появления инцидентов",
									 labels={'x':'Время','y':'Суммарно инцидентов'})
	chart_data.update_layout(title={
		'font_size':16,
		'xanchor':'center',
		'x':0.5,
	})
	return chart_data.to_html()

def get_rounded_chart(data:dict):
	values = list() 
	labels = ['Легетимных', 'Не определено',  'Нарушенией']
	for key in data:
		if key!='all':
			values.append(data[key])
	chart_data = Figure(data=[Pie(labels=labels, values=values, textinfo='label+percent', pull=[0, 0, 0.2], hole=.3)])		
	chart_data.update_layout(title_text='Распределение типов инцидентов')
	chart_data.update_layout(title={
		'font_size':16,
		'xanchor':'center',
		'x':0.5,
	})
	
	return chart_data.to_html()

