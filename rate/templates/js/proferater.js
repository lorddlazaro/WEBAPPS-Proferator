$(document).ready(function(){
	$("#info").popover({
		placement: "bottom",
		trigger: "click",
	});

	$('#next').click(function(){
		if($('#factor').text()=="Fair in Grading"){
			$('#factor').text('Clear');
			$(".progress-bar").css("width", "37.5%");
		}
		else if($('#factor').text()=="Clear"){
			$(".progress-bar").css("width", "50%");
			$('#factor').text('Knowledgeable');
		}
		else if($('#factor').text()=="Knowledgeable"){
			$(".progress-bar").css("width", "62.5%");
			$('#factor').text('Engaging');
		}
		else if($('#factor').text()=="Engaging"){
			$(".progress-bar").css("width", "75%");
			$('#factor').text('Fair on Workload');
		}
		else if($('#factor').text()=="Fair on Workload"){
			$(".progress-bar").css("width", "87.5%");
			$('#factor').text('Considerate');
		}
		else if($('#factor').text()=="Considerate"){
			$(".progress-bar").css("width", "100%");
			$('#factor').text('Approachable');
		}
		else if($('#factor').text()=="Approachable"){
			$('nextButton').prop('disabled', true);
		}
	});

	$('#back').click(function(){
		if($('#factor').text()=="Fair in Grading"){
			$(".progress-bar").css("width", "25%");
			$('backButton').prop('disabled', true);
		}
		else if($('#factor').text()=="Clear"){
			$(".progress-bar").css("width", "25%");
			$('#factor').text('Fair in Grading');
		}
		else if($('#factor').text()=="Knowledgeable"){
			$(".progress-bar").css("width", "37.5%");
			$('#factor').text('Clear');
		}
		else if($('#factor').text()=="Engaging"){
			$(".progress-bar").css("width", "50%");
			$('#factor').text('Knowledgeable');
		}
		else if($('#factor').text()=="Fair on Workload"){
			$(".progress-bar").css("width", "62.5%");
			$('#factor').text('Engaging');
		}
		else if($('#factor').text()=="Considerate"){
			$(".progress-bar").css("width", "75%");
			$('#factor').text('Fair on Workload');
		}
		else if($('#factor').text()=="Approachable"){
			$(".progress-bar").css("width", "87.5%");
			$('#factor').text('Considerate');
			$('nextButton').prop('disabled', false);
		}
	});

	$('#cancel').click(function(){
		if(!rcFormEmpty()){
			alert("Are you sure you want to leave?");
		}
		else {
			alert("Bye!");
		}
	});

	$('#submit').click(function(){
		alert("Submit is clicked");
	});

	

});


function rcFormEmpty() {
	if ($("textArea#message").val() == "") {
	    return true;
	}
	return false;
}


/*$(".progress-bar").css("width", "14.2857143%");*/


