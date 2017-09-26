function getQuestion(input) {
    $.ajax({
        type: "POST",
        url: "/backend/getquestion.py",
        data: { param: input },
        success: callbackFunc
    });
}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
    document.write(response)
}

function main(){
 	alert('Second alert...');
 	console.log('in js main');
 	('.question').text("next question is ...");
}

$(document).ready(main);