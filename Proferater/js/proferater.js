$(document).ready(function(){
	$("#info").popover({
		placement: "bottom",
		trigger: "click",
	});

	$('#next').click(function(){
		if($('#factor').text()=="Fair Grade"){
			$('#factor').text('Clear');
		}
		else if($('#factor').text()=="Clear")
			$('#factor').text('Knowledgeable');
		else if($('#factor').text()=="Knowledgeable")
			$('#factor').text('Engaging');
		else if($('#factor').text()=="Engaging")
			$('#factor').text('Fair Workload');
		else if($('#factor').text()=="Fair Workload")
			$('#factor').text('Considerate');
		else if($('#factor').text()=="Considerate")
			$('#factor').text('Approachable');
		else if($('#factor').text()=="Approachable")
			$('nextButton').prop('disabled', true);
	});

	$('#back').click(function(){
		if($('#factor').text()=="Fair Grade")
			$('backButton').prop('disabled', true);
		else if($('#factor').text()=="Clear")
			$('#factor').text('Fair Grade');
		else if($('#factor').text()=="Knowledgeable")
			$('#factor').text('Clear');
		else if($('#factor').text()=="Engaging")
			$('#factor').text('Knowledgeable');
		else if($('#factor').text()=="Fair Workload")
			$('#factor').text('Engaging');
		else if($('#factor').text()=="Considerate")
			$('#factor').text('Fair Workload');
		else if($('#factor').text()=="Approachable"){
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

	if($(".progress-bar").css("width") == $(".progress").css("width")){
		$('button#submit').prop('disabled', false);
	    if(!$('button#submit').prop('disabled')){
	    	alert("enabled!");
	    }
	}
});


function rcFormEmpty() {
	if ($("textArea#message").val() == "") {
	    return true;
	}
	return false;
}


$(".progress-bar").css("width", "100%");


