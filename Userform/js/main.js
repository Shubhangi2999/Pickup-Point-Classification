var data;
var iCnt = 0;
$(document).ready(function() {
  $('#btAdd').on('click', function() {
    iCnt = iCnt + 1;
    var newField = '<div id="resd' + iCnt + '"> <input style= "width: 470px" type="text" name="link1" id=tb' + iCnt + ' ' + '> </div>';
    $('#resd').append(newField);
  });

  $('#btRemove').click(function() {
    if (iCnt != 0) {
      $('#tb' + iCnt).remove();
      $('#resd' + iCnt).remove();
      iCnt = iCnt - 1;
    }
  });
});


function GenerateDataModal(response) {
  console.log(response);
  response=JSON.parse(response);
  response.residential=(JSON.stringify(response.residential))
  var b = "";
  b="<div class='boxed'><br><h4 style='text-align: center'><b>RECEIVED DETAILS</b></style></h4><div class='div2'>"+"<b>Name of the Applicant: </b>"+(response.name)+
    "<br><b>Email Id: </b>"+(response.email)+"<br><b>Phone No: </b>"+(response.phone)+"<br><b>Location Name: </b>"+(response.location_name)+"<br><b>Location Type: </b>"+(response.location_type)+
    "<br><b>Address: </b>"+(response.address)+"<br><b>City: </b>"+(response.city)+"<br><b>Nearby residential areas: </b>"+(response.residential)+"<br><b>Length: </b>"+(response.length)+
    "<br><b>Breadth: </b>"+(response.breadth)+"<br><b>Height: </b>"+(response.height)+"<br><b>Opening Timings: </b>"+(response.open_time)+"<br><b>Closing Timings: </b>"
	+(response.close_time)+"<br><b>Disabled Friendly: </b>"+(response.disabled)+"<br><b>Owned/Rented: </b>"+(response.owned_rented)+"<br><b>Staff Count: </b>"+(response.staff_count)
	+"<br><b>Age of the Location: </b>"+(response.store_age)+"<br><b>Average Daily Footfall: </b>"+(response.visitors)+"<br><b>No. of Working Days: </b>"+(response.working_days)+"</div></div>";
  var ele = document.getElementById("modalbody2");
  ele.innerHTML = b;
  $('#modal-button2').click();
}

function GenerateModal(response) {
  console.log(response);
  var a = ""
  a="<div class='div1'>"+"<b>AMAZON LOCKER APPLICATION</b></div><br>"+"<div class='boxed'><br><h4 style='text-align: center'><b>ALERT!!!</b></style></h4><div class='div2'>"+
  "<b>"+response+"</b></div></div>"
  var element = document.getElementById("modalbody1");
  element.innerHTML = a;
  $('#modal-button').click();
}

function checkerror(){
  var Namere = /[A-Za-z]{1}[A-Za-z]/;
  if (!Namere.test($("#name_input").val())) {
    GenerateModal("Name can not have less than 2 characters.");
    return;
  }

  var mobilere = /^\d{10}$/;
  if (!mobilere.test($("#phone_input").val())) {
    GenerateModal("Please enter valid mobile number.");
    return;
  }

  if ($("#email_input").val()=="") {
    GenerateModal("Please enter your email id.");
    return;
  }

  var reeamil = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,6})?$/;
  if (!reeamil.test($("#email_input").val())) {
    GenerateModal("Please enter valid email address.");
    return;
  }

  if ($("#city_input").val()=="") {
    GenerateModal("Please enter your city.");
    return;
  }

  if ($("#location_name").val()=="") {
    GenerateModal("Please enter location name.");
    return;
  }

  if ($("#location_type").val()=="Select") {
    GenerateModal("Please enter location type.");
    return;
  }


  if ($("#address_input").val()=="") {
    GenerateModal("Please enter address of location.");
    return;
  }


  if ($("#tb0").val()=="") {
    GenerateModal("Please enter address of atleast one nearby residential area.");
    return;
  }

  var i;
  for (i = 1; i <= iCnt; i++) {
    if ($("#tb" + i).val()=="") {
      GenerateModal("You cannot leave nearby residential area blank.");
      return;
    }
  }

  if (($("#area_dimensions1").val()=="") || ($("#area_dimensions2").val()=="") || ($("#area_dimensions3").val()=="")){
    GenerateModal("Please enter dimensions of area available for locker installation.");
    return;
  }

  if((!(document.getElementById('disabled_yes').checked)) &&(!(document.getElementById('disabled_no').checked)))  {
    GenerateModal("Please enter whether the location is accessible by disabled people? ");
    return;
  }

  if((!(document.getElementById('owned').checked)) &&(!(document.getElementById('rented').checked)))  {
    GenerateModal("Please select one button either owned or rented");
    return;
  }

  if ($("#visitors_input").val()=="") {
    GenerateModal("Please enter average number of visitors per day for your store.");
    return;
  }


  if ($("#staff_count").val()=="") {
    GenerateModal ("Please enter the staff count at your store.");
    return;
  }

  if ($("#age_input").val()=="") {
    GenerateModal("Please enter the age of your store.");
    return;
  }

  if ($("#working_days").val()==""){
    GenerateModal("Please enter the number of working days of your store.");
    return;
  }

  if ($("#timings_open").val()==""){
    GenerateModal("Please enter the opening time of your store.");
    return;
  }

  if ($("#timings_close").val()==""){
    GenerateModal("Please enter the closing time of your store.");
    return;
  }
  else {
    var name = $("#name_input").val();
    var phone = $("#phone_input").val();
    var email = $("#email_input").val();
    var location_type = $("#location_type").val();

    if ($("#location_type").val()=="Restaurant") {
      location_type = "restaurant";
    }
    else if ($("#location_type").val()=="Shopping Mall") {
      location_type = "shopping_mall";
    }
    else if ($("#location_type").val()=="Store") {
      location_type = "store";
    }
    else if ($("#location_type").val()=="Supermarket") {
      location_type = "supermarket";
    }


    var location_name = $("#location_name").val();
    var city = $("#city_input").val();
    var disabled;
    if(document.getElementById('disabled_yes').checked){
      disabled = $("#disabled_yes").val();
    }
    else{
      disabled = $("#disabled_no").val();
    }
    var visitors = $("#visitors_input").val();
    var owned_rented;
    if(document.getElementById('owned').checked){
      owned_rented = $("#owned").val();
    }
    else{
      owned_rented = $("#rented").val();
    }
    var store_age = $("#age_input").val();
    var staff_count = $("#staff_count").val();
    var open_time = $("#timings_open").val();
    var close_time = $("#timings_close").val();
    var working_days = $("#working_days").val();
    var residential = {};

    for (i = 0; i <= iCnt; i++) {
      residential[i] = ($("#tb"+i)).val();
    }

    var address = $("#address_input").val();
    var length = $("#area_dimensions1").val();
	var breadth = $("#area_dimensions2").val();
	var height = $("#area_dimensions3").val();
	
    data = {
      name : name,
      phone : phone,
      email : email,
      location_type : location_type,
      location_name : location_name,
      city : city,
      open_time : open_time,
      close_time : close_time,
      disabled : disabled,
      visitors : visitors,
      owned_rented : owned_rented,
      store_age : store_age,
      staff_count : staff_count,
      residential : residential,
      address : address,
      length : length,
	  breadth : breadth,
	  height: height,
      working_days : working_days
    };
    var data1 = JSON.stringify(data);
    GenerateDataModal(data1);
  }
}

function submitToAPI(e) {
  e.preventDefault();
  data= {MessageBody: JSON.stringify(data)};

  $.ajax({
    type: "GET",
    url : "https://vt9wmqkxve.execute-api.us-east-2.amazonaws.com/Deploy/v1/send",
    dataType: "json",
    crossDomain: "true",
    contentType: "application/json; charset=utf-8",
    data: data,
    success: function () {
      alert("Your details have been submitted successfully. We will get back to you via email soon.");
      document.getElementById("locker_app_form").reset();
      location.reload();
    },
    error: function () {
      alert("Form submission failed.");
    }
  });
}
