// // build metadata and charts

// 	function buildMetadata(state) {

// 		var selector = d3.select("#state-metadata")
	
// 		d3.json(`/metadata/${state}`).then((data) => {
// 		  selector.html("");
	
// 		  Object.entries(data).forEach(([key, value]) => {
// 			selector.append("h3").text(`${key}: ${value}`);
// 		  });
		  
// 	  })
	
	
// 	function buildCharts(state) {

// 	  // @TODO: Use `d3.json` to fetch the state data for the plots
// 	  d3.json(`/states/${state}`).then((data) => {
	
// 		  var trace = {
// 			labels: ["public4Year_total", "public4Year_outofstateTotal", "privateTotal", "public2YInState"],
// 			values: [data] ,
// 			type: "pie",
// 		  }
	
// 		  var data = [trace]
	
// 		  var layout = {
// 			title: `Tuitions for: ${state}`,
			
// 		  };
// 		  var PIE = document.getElementById("pie");
	
// 		  Plotly.newPlot(PIE, data, layout, {responsive: true});
// 		})
// 	}
// 	}
// 	function init() {
// 	  // Grab a reference to the dropdown select element
// 	  var selector = d3.select("#selDataset");
	
// 	  // Use the list of state names to populate the select options
// 	  d3.json("/states").then((stateNames) => {
// 		stateNames.forEach((state) => {
// 		  selector
// 			.append("option")
// 			.text(state)
// 			.property("value", state);
// 		});
	
// 		// Use the first state from the list to build the initial plots
// 		const firstState = stateNames[0];
// 		buildCharts(firstState);
// 		buildMetadata(firstState);
// 	  });
// 	}
	
// function optionChanged(newState) {
// 	  // Fetch new data each time a new state is selected
// 	  buildCharts(newState);
// 	  buildMetadata(newState);
// 	}
	
// 	// Initialize the dashboard
// 	init();


var tuition = ["public4Year_total", "public4Year_outofstateTotal", "privateTotal", "public2YInState"]


// d3.csv("sample.csv", function(d) {

// 		return {
// 			state: d.State,
// 			private_total: +d.privateTotal
// 		}

// 		var trace_high = {
// 		x: d.State, 
// 		y: d.privateTotal,
// 		name: 'privateTotal',
// 		type: 'scatter', 
// 	mode: 'lines'}
	
// 		var data = [trace_high]

// 		var layout = {
// 			title: "Tuition College",
			
// 		  };
	  
// 		var LINE = document.getElementById('line');
//       Plotly.newPlot(LINE, data, layout) 
// 		})