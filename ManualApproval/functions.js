
var sock = new WebSocket("wss://e79ojx5x0h.execute-api.us-east-2.amazonaws.com/deploy");
var storeid;

/* Used to establish the socket connection. */
sock.onopen = function(event) {
	console.log("Connection established");
	sock.send(JSON.stringify({"action" : "getTableData"}));
	sock.onmessage = function (event) {
		GenerateTable(event.data);
		clickrow();
	}
}
  
/* Sends final status (Accepted/Rejected) of an application recognized
	by its store id. */
function sendFinalStatusToAPI(e,val){
	e.preventDefault();
	var stat = val;
	var data = {
		"store_id" : JSON.parse(storeid),
		"status_ar" : stat
	};
	data = JSON.stringify(data);
	sock.send(JSON.stringify({"action" : "updateStatus", "data" : data}));
	sock.onmessage = function (event) {
		alert(event.data);
	}		
}

/* Sends the store id corresponding to which the user wants to get the data
to display in the modal. */
function submitToAPI(storeid){		
	var data=JSON.parse(storeid);
	data = JSON.stringify(data);
	sock.send(JSON.stringify({"action" : "getDataForStoreID", "data" : data}));
	sock.onmessage = function (event){
		console.log(event.data);
		GenerateModal(event.data);
	}
}
 
/* For the functionality of clicking on any row of th table to get data corresponding to it. */
function clickrow()
{
	$('tr').click(function(){
		storeid=($(this).html())[4];
		submitToAPI(storeid);
	});
}
	
/* Used to dynamically generate table from the data that is received from the backend. */	
function GenerateTable(response){
    
	var table_data = response;
	table_data = JSON.parse(table_data);
	var applicants=new Array();
	applicants.push(["Store Id","Name","Store Name","Location Type","City"])
	
	for(var i=0;i<table_data.length;i++)
	{
		applicants.push(table_data[i]);
	}
	
	applicants.sort(function(a, b){ return a[0] - b[0];});
	var table= document.createElement("TABLE");
	table.setAttribute('class', 'responstable');
	var row;
	row = table.insertRow(-1);
	
	for (var i = 0; i < 5; i++) {
		var headerCell = document.createElement("TH");
		headerCell.innerHTML = applicants[0][i];
		row.appendChild(headerCell);
	}
		
	for (var i = 1; i < applicants.length; i++) {
		var loc_type = applicants[i][3];
		loc_type = loc_type.replace(/_/g, ' ');
		loc_type = loc_type.charAt(0).toUpperCase() + loc_type.slice(1);
		applicants[i][3] = loc_type;
	}

	for (var i = 1; i < applicants.length; i++) {
		row = table.insertRow(-1);
		for (var j = 0; j < 5; j++) {
			var cell = row.insertCell(-1);
			cell.innerHTML = applicants[i][j];
		}
	}

	var dvTable = document.getElementById("dvTable");
	dvTable.innerHTML = "";
	dvTable.appendChild(table);
}

/* Used to generate the modal for the application the user clicked on in the table.*/
function GenerateModal(response){
	var data = response;
	data=JSON.parse(data);
	
	var string = data.location_type;
	string = string.replace(/_/g, ' ');
	data.location_type = string.charAt(0).toUpperCase() + string.slice(1);
	
	var residentials = "<br> ";
	var keys = Object.keys(data.distance_from_residential);
	for(var i = 0; i < keys.length; i++)
	{
		residentials += "<b>" + (i+1) + ". </b>" + keys[i] + " : " + data.distance_from_residential[keys[i]] + "<br>";
	}
	
	var html_data = ""
	html_data = "<div class='bodycontent'><div class='div1'><b>"+(data.location_name)+"<br>PREDICTED QOS: </b>"+(data.qos)+"/5<br><b>AUTOMATED SUGGESTION: </b>"+(data.suggest)
		+"</b></div><br><div id='parent1'><div class='leftboxed'><h4 style='text-align: center'><b>APPLICANT DETAILS</b></style></h4><div class='div2'>"	
		+"<b>Name of the Applicant: </b>"+(data.name)+"<br><b>Email Id: </b>"+(data.email)+"<br><b>Phone No: </b>"+(data.phone_no)+"</div></div>"
		+"</b></div><div class='rightboxed'><h4 style='text-align: center'><b>LOCATION DETAILS</b></style></h4><div class='div2'>"
		+"<b>Location Type: </b>"+(data.location_type)+"<br><b>Address: </b>"+(data.address)+"<br><b>City: </b>"+(data.city)+"</div></div></div>"
		+"<br><br><br><br><br><br><br><br><br><br><div id='parent1'><div class='leftboxed1'><h4 style='text-align: center'><b>GOOGLE DATA</b></style></h4><div class='div2'>"
		+"<b>Google Rating: </b>"+(data.rating)+"<br><b>No. of Bus Stations: </b>"+(data.no_busstns)+"<br><b>No of user reviews: </b>"
		+(data.no_of_reviews)+"<br><b>No of Parkings: </b>"+(data.no_parkings)+"<br><b>Distance from nearby residential areas: </b>"
		+(residentials)+"</div></div>"+"<div class='rightboxed1'><h4 style='text-align: center'><b>OPERATIONAL DETAILS</b></style></h4><div class='div2'>"
		+"<b>Area Dimensions: </b>"+(data.area_dimensions)+"<br><b>Opening Timings: </b>"+(data.open_time)+"<br><b>Closing Timings: </b>"
		+(data.close_time)+"<br><b>Disabled Friendly: </b>"+(data.disabled)+"<br><b>Owned/Rented: </b>"+(data.owned_rented)+"<br><b>Staff Count: </b>"
		+(data.staff_count)+"<br><b>Age of the Location: </b>"+(data.store_age)+"<br><b>Average Daily Footfall: </b>"+(data.visitors)
		+"<br><b>No. of Working Days: </b>"+(data.working_days)+"</div></div></div></div>";
		
	var element = document.getElementById("modalbody");
	element.innerHTML = html_data;
	$('#modal-button').click();
}