function toggle_display1(){
  el = document.querySelector('.patient_form_content_section');

  if(el.style.display == 'none'){
      el.style.display = 'block'
  }else{
     el.style.display = 'none'
  }
}

function toggle_display2(){
  el = document.querySelector('.clients_display');

  if(el.style.display == 'none'){
      el.style.display = 'block'
  }else{
     el.style.display = 'none'
  }
}