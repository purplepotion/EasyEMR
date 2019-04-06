function toggle_display(){
  el = document.querySelector('.patient_form_content_section');

  if(el.style.display == 'none'){
      el.style.display = 'block'
  }else{
     el.style.display = 'none'
  }
}