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
        question : "Within the past 3 months, have you gotten a piercing or tattoo?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
    },{
        question : "Within the past 3 weeks, have you received a vaccination?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "Could you currently be pregnant?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "Within the past 72 hours, have you had any dental surgery including a tooth pulling?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "Have you, for any reason, have a blood transfusion within the past 6 months?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "Many medications that affect your blood such as Aspirin or Warfarin can make you inelgible. Within the past 14 days, have you taken any blood medication",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "We currently do not accept users who use illegal drugs, have you ever used an illegal drug?(excluding cannabis)",
        choiceA : "Yes",
        choiceB : "No",
        correct : "B"
      },{
        question : "More sensitive medical questions will be asked in your pre-donation interview. Do you swear that your answers given are so far are 100% truthful?",
        choiceA : "Yes",
        choiceB : "No",
        correct : "A"
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
    warning.style.display = "none"
    renderQuestion();
    quiz.style.display = "block";
}

// checkAnwer

function checkAnswer(answer){
    if( answer == questions[runningQuestion].correct){
      if(runningQuestion < lastQuestion){
        runningQuestion++;
        renderQuestion();
    }else{
      choiceA.style.display = "none"
      choiceB.style.display = "none"
      question.style.display = "none"
      continueB.style.display = "block"
      success.style.display = "block"
      // end the quiz and show the score
    }
    }else{
        // answer is wrong
        // change progress color to red
        location.assign('/questionnairefail');
        
      
    }
}