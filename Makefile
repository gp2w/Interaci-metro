html:
	# Now build the app
	cp examples/dash.py app.py
	export DEBUG=False && python3 app.py &
	sleep 30
	wget -r http://127.0.0.1:8050/ 
	wget -r http://127.0.0.1:8050/_dash-layout 
	wget -r http://127.0.0.1:8050/_dash-dependencies
	sed -i 's/_dash-layout/_dash-layout.json/g' 127.0.0.1:8050/_dash-component-suites/dash_renderer/*.js 
	sed -i 's/_dash-dependencies/_dash-dependencies.json/g' 127.0.0.1:8050/_dash-component-suites/dash_renderer/*.js
	# Add our head
	# sed -i '/<head>/ r head.html' 127.0.0.1:8050/index.html
	mv 127.0.0.1:8050/_dash-layout 127.0.0.1:8050/_dash-layout.json	
	mv 127.0.0.1:8050/_dash-dependencies 127.0.0.1:8050/_dash-dependencies.json

	cp static/async* 127.0.0.1:8050/_dash-component-suites/dash_core_components/
	cp static/async-table* 127.0.0.1:8050/_dash-component-suites/dash_table/

	ps | grep python | awk '{print $$1}' | xargs kill -9

clean:
	rm -rf 127.0.0.1:8050/