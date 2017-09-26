// function getQuestion() {
// 	$.getJSON('backend/app.py', {}, function(data) {
//         				$(".question").text(data.question);
//         				alert(data.question)
//         			})
// }


// function postFeedback() {
//     $('.score1').bind('click', function() {
// 		$.getJSON('http://127.0.0.1:5000/', {
// 		        	new_notes: $('input[name="notes"]').val(),
// 		        	id_q: '2',
// 		        	new_grade: '3'
// 		      		}, function(data) {
//         				$(".question").text(data.question);
//         			}
//       });
//       return false;
//     });
// };

function main(){
	$.getJSON( 'http://127.0.0.1:5000/', function( data ) {
	 	alert('Third alert...');
	 });
	alert('Second alert...')
};

$(document).ready(main);