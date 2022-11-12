const rangeInput = document.querySelectorAll(".range-input input"),
progress =  document.querySelector(".slider_price .progress"),
priceInput = document.querySelectorAll(".price_input .input-min , .input-max");
priceInput.forEach(input=>{
    input.addEventListener("input",e=>{
        let minVal = parseInt(priceInput[0].value),
        maxVal = parseInt(priceInput[1].value);

        if ((maxVal-minVal >= 100 )&& maxVal<=1000000){
            if(e.target.className==="input-min"){
                rangeInput[0].value=minVal;
                progress.style.left=(minVal / rangeInput[0].max) *100 +"%";
            }
            else{
                rangeInput[1].value=maxVal;
                progress.style.right= 100 - (maxVal / rangeInput[1].max) *100 +"%";
            }
            
        }
    })
});

function iii(){
if(document.querySelector('.filter_btnControl').checked===false){
    document.querySelector('.filter_block').style='right:0;';
}
if(document.querySelector('.filter_btnControl').checked===true){
    document.querySelector('.filter_block').style='right:-300;';
}
}
rangeInput.forEach(input=>{
    input.addEventListener("input",e=>{
        let minVal = parseInt(rangeInput[0].value),
        maxVal=parseInt(rangeInput[1].value);

        if (maxVal-minVal<100){
            if(e.target.className==="range-min"){
                rangeInput[0].value=maxVal-100;
            }else{
                rangeInput[1].value=minVal-100;
            }
            
        }else{
            priceInput[0].value=minVal;
            priceInput[1].value=maxVal;
            progress.style.left=(minVal / rangeInput[0].max) *100 +"%";
            progress.style.right= 100 - (maxVal / rangeInput[1].max) *100 +"%";
        }
    })
});