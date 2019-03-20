
let days    = document.querySelector('.days'),
    hours   = document.querySelector('.hours'),
    minutes = document.querySelector('.minutes'),
    seconds = document.querySelector('.seconds');

let timeInSeconds = document.querySelector('#time-in-seconds');
let couponValue = document.querySelector('#coupon-value');


function timeShape(num){
  return num.toString().length < 2? '0'+num: num;
}

function secondsToHours(seconds){
  let days, hours, minutes;

  days = parseInt(seconds/ (3600*24))
  seconds %= (3600*24)
  hours = parseInt(seconds/3600);
  seconds %= 3600;
  minutes = parseInt( seconds/60 );
  seconds %= 60;
  
  return `${timeShape(days)}:${timeShape(hours)}:${timeShape(minutes)}:${timeShape(seconds)}`
}


// interval to decremant the timer
console.log('strat');
let gamesTimer = setInterval(()=>{
  let v = parseInt(timeInSeconds.value);
  
  console.log('value', v);
  
  if(v > 0){
    timeInSeconds.value = v - 1
    let time = secondsToHours(v-1);
    [days.innerText, hours.innerText, minutes.innerText, seconds.innerText] = time.split(':')
  }
},1000);

// event on get coupon btns
let elms = document.querySelectorAll('.btn');
elms.forEach(elm=>{
  elm.addEventListener('click', (e)=>{
    alert( couponValue.value )
  });
});

// event on small images
let smallImgs = document.querySelectorAll('.small-imgs img');
let mainImg = document.querySelector('.main-img img');

smallImgs.forEach(elm=>{
  elm.addEventListener('mouseover', (e)=>{
    console.log()
    mainImg.src = elm.dataset.large;
  });
})


//# sourceMappingURL=main.js.map
