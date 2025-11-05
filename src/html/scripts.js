






document.getElementById('notes-toggle-switch').checked = false;
document.getElementById('brackets-toggle-switch').checked = true;
document.getElementById('rid-toggle-switch').checked = false;



set_up_toggle_by_class('nte-toggle-switch', '.display_NTE');
set_up_toggle_by_class('npr-toggle-switch', '.display_NPR');
set_up_toggle_by_tag('notes-toggle-switch', 'NTE');
set_up_toggle_by_tag('notes-toggle-switch', 'NPR');
set_up_toggle_by_tag('notes-toggle-switch', 'AST');

set_up_toggle_by_class('eng-toggle-switch', '.display_ENG', 'inline');
set_up_toggle_by_class('met-toggle-switch', '.display_MET', 'inline');

toggle_bracket_style('brackets-toggle-switch', '.brackets')

set_up_toggle_by_class('rid-toggle-switch', '.display_RID');
set_up_toggle_by_class('add-toggle-switch', '.display_ADD', 'inline');
set_up_toggle_by_class('del-toggle-switch', '.display_DEL', 'inline');



all_tags = Array('A', 'B', 'C')
function setup_all_toggles(tag_array) {
    tag_array.forEach((element) => {
        
    })
}
// setup_all_toggles(all_tags)





function set_up_toggle_by_tag(toggle_element_id, target_elements_tag_name, display_style='inline') {
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


function set_up_toggle_by_class(toggle_element_id, target_elements_class_name, display_style='inline') {
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


function toggle_bracket_style(toggle_element_id, target_elements_class_name) {
    let toggle_element = document.getElementById(toggle_element_id)
    let target_elements = document.querySelectorAll(target_elements_class_name)
    toggle_element.addEventListener('change', () => {
        target_elements.forEach( item => {
            if (toggle_element.checked) {
                item.style.backgroundColor = 'yellow';
            } else {
                item.style.backgroundColor = 'transparent';
            }
        })
    })
}


let topButton = document.getElementById("topBtn");
let menuButton = document.getElementById("menuBtn");
menuButton.onclick = function() {toggleMenu()};

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    topButton.style.display = "block";
  } else {
    topButton.style.display = "none";
  }
}


function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

function toggleMenu() {
    let menuElement = document.querySelector('.user-selections');
    let mainElement = document.querySelector('main');
    if (menuElement.style.display == 'none') {
        menuElement.style.display = 'block';
        mainElement.style.marginTop = '200px';
    } else {
        menuElement.style.display = 'none';
        mainElement.style.marginTop = '72px';
    }
}