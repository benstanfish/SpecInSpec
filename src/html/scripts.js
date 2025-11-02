

document.getElementById('notes-toggle-switch').checked = true;

set_up_toggle_by_class('npr-toggle-switch', '.display_NPR');
set_up_toggle_by_tag('notes-toggle-switch', 'NPR');
set_up_toggle_by_tag('notes-toggle-switch', 'AST');
set_up_toggle_by_class('eng-toggle-switch', '.display_ENG', 'inline');
set_up_toggle_by_class('met-toggle-switch', '.display_MET', 'inline');




function set_up_toggle_by_tag(toggle_element_id, target_elements_tag_name, display_style='inherit') {
    let toggle_element = document.getElementById(toggle_element_id)
    let target_elements = document.querySelectorAll(target_elements_tag_name)
    toggle_element.addEventListener('change', () => {
        target_elements.forEach( item => {
            if (toggle_element.checked) {
                item.style.display = display_style;
            } else {
                item.style.display = 'none';
            }
        })
    })
}

function set_up_toggle_by_class(toggle_element_id, target_elements_class_name, display_style='inherit') {
    let toggle_element = document.getElementById(toggle_element_id)
    let target_elements = document.querySelectorAll(target_elements_class_name)
    toggle_element.addEventListener('change', () => {
        target_elements.forEach( item => {
            if (toggle_element.checked) {
                item.style.display = display_style;
            } else {
                item.style.display = 'none';
            }
        })
    })
}







// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}