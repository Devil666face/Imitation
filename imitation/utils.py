from imitation.models import Incident
import plotly.express

def get_main_chart():
	incident_list = Incident.objects.all().order_by('created_at')
	y_list = list()
	x_list = list()
	for index,incident in enumerate(incident_list):
	    y_list.append(index+1)
	    x_list.append(incident.created_at)
	print(y_list)
	print(x_list)
	chart_data = plotly.express.line(x=list(reversed(x_list)),
									 y=list(reversed(y_list)),
									 title="График появления инцидентов",
									 labels={'x':'Время','y':'Суммарно инцидентов'})
	chart_data.update_layout(title={
		'font_size':22,
		'xanchor':'center',
		'x':0.5,
	})
	return chart_data.to_html()
