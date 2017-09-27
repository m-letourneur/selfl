function getQuestion() {
	$.getJSON('http://127.0.0.1:5000/req', function(data) {
        				$(".question").text(data.question);
        				console.log(id_q);
        				id_q = data.id_q;
        				console.log(id_q);
        			})
}

function postFeedback() {
	$('.score1').bind('click', function() {
		$.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/req',
            data: JSON.stringify( {new_notes: $('input[name="notes"]').val(),
		        id_q: id_q,
		        new_grade: $(this).val()} ),
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(data){
            	console.log(data);
				id_q = data.id_q;
				console.log(id_q);
				//Clear the notes
				console.log($('input[name="notes"]'))
				$('input[name="notes').val('');
				getQuestion();
			},
    	    failure: function(errMsg) {
	        	alert(errMsg);}
	    });
	});
}

function hitHint(){
	$('.hint').bind('click', function() {
	 var url = 'http://127.0.0.1:5000/hint/'
	 $.getJSON(url.concat(id_q), function(data) {
        				id_q = data.id_q;
        				var notes = data.notes;
        				alert("Helping you on this with: ".concat(notes));
        			})
	});
}

function main(){
	getQuestion();
	postFeedback();
	hitHint();
};

var id_q = 0;
var new_grade = -1;
$(document).ready(main);