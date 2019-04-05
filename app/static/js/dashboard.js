function toggle_display(){
  el = document.querySelector('.patient_form_content_section');

  if(el.style.visibility == 'hidden'){
      el.style.visibility = 'visible'
  }else{
     el.style.visibility = 'hidden'
  }
}