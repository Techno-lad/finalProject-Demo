let Gpa = 0.0;
var intervention;
var normalGpa;
var honorRoll;

function play() {
  var audio = new Audio('https://notificationsounds.com/message-tones/juntos-607/download/mp3');
  audio.play();
  
}




// Set the date we're counting down to


function getRndInteger(min, max) {
  

  var Gpa = Math.floor(Math.random() * (max - min)) + (Math.floor(Math.random()*10))/10;

  
if (Gpa <= 2.0){
  play();
  intervention = true;
  alert("Your Gpa is:"+ Gpa +  "You are at risk of academic suspension." );

}
else if (Gpa >=2.1 && Gpa <=3.4){
  play();
  normalGpa = true;
  alert("Your Gpa is:" + Gpa + "Keep up the good work!" );
  
}
else if (Gpa > 3.5){
  play();
  let honorRoll = true;
  alert("Your Gpa is: " + Gpa + "Absolutely brilliant." + "😎" );
}



}