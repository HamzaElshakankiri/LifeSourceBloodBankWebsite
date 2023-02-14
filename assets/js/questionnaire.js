// select all elements
const start = document.getElementById("start");
const quiz = document.getElementById("quiz");
const question = document.getElementById("question");
const choiceA = document.getElementById("A");
const choiceB = document.getElementById("B");

// create our questions
let questions = [
    {
        question : "Do you feel well today?",
        choiceA : "Yes ",
        choiceB : "No",
        correct : "A"

    },{
        question : "Within the past 3 months, have you gotten a Piercing or Tattoo?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
    },{
        question : "Have you recently received a Vaccine?(within the past 3 weeks)",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "Could you currently be pregnant ",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      }
];

// create some variables

const lastQuestion = questions.length - 1;
let runningQuestion = 0;
let count = 0;

// render a question
function renderQuestion(){
    let q = questions[runningQuestion];

    question.innerHTML = "<p>"+ q.question +"</p>";
    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;

}

start.addEventListener("click",startQuiz);

// start quiz
function startQuiz(){
    start.style.display = "none";
    renderQuestion();
    quiz.style.display = "block";
}

// checkAnwer

function checkAnswer(answer){
    if( answer == questions[runningQuestion].correct){
        // answer is correct

        // change progress color to green
       
    }else{
        // answer is wrong
        // change progress color to red
        alert("You should wait to donate")
        location.reload()
      
    }
    count = 0;
    if(runningQuestion < lastQuestion){
        runningQuestion++;
        renderQuestion();
    }else{
        // end the quiz and show the score
        location.reload()
    }
}