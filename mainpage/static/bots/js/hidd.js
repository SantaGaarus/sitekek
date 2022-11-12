function hid(){
    logos.style='visibility:hidden';
  document.querySelectorAll('.hidden_link3')[0].style='display:none';
  document.querySelectorAll('.hidden_link4')[0].style='display:none';
  document.querySelectorAll('.hidden_link3')[1].style='display:none';
  document.querySelectorAll('.hidden_link4')[1].style='display:none';
  document.querySelectorAll('.hidden_link3')[2].style='display:none';
  document.querySelectorAll('.hidden_link4')[2].style='display:none';
  document.querySelector('.text_input').style="display:none";
  }
  document.querySelector('.vsio').onmouseenter=()=>{
    hid();
  }