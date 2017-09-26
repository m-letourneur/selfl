function getQuestion(id) {
	$.getJSON('http://127.0.0.1:5000/req', function(data) {
        				$(".question").te
        				console.log(id)
        			})
	return id;

}

function postFeedback(id) {
	$('.score1').bind('click', function() {
		$.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000/req',
            data: JSON.stringify ({new_notes: $('input[name="notes"]').val(),
		        id_q: id,
		        new_grade: $(this).val()}),
            contentType: "application/json",
            dataType: 'json',
            success: function(data){
            	console.log(data);
				// alert(data.new_notes)
				id_q = getQuestion(data.id_q);
            }
        });
	});
	return id;
}

function main(){
	var id_q = 0;
	var new_grade = -1;
	console.log(id_q);
	id_q = getQuestion(id_q);
	console.log(id_q);
	id_q = postFeedback(id_q);
	console.log(id_q);
};

$(document).ready(main);