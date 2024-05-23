const xmark=document.querySelector('.xmark')
const hamburger=document.querySelector('.hamburger')
const hamMenu=document.querySelector('.hamburger-menu')

function hideSuccess() {
    const success = document.querySelector('.alert-success');
    
    if (success.style.display !== 'none') {
        success.style.display = 'none';
    }

}


setInterval(hideSuccess, 3000);


function hideWarning() {
    const warning=document.querySelector('.alert-warning');
    
    if (warning.style.display !== 'none') {
        warning.style.display = 'none';
    }

}

setInterval(hideWarning, 3000);


function hideDanger() {
    const danger = document.querySelector('.alert-danger'); 
    if (danger.style.display !== 'none') {
        danger.style.display = 'none';
    }

}

setInterval(hideDanger, 3000);

hamburger.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('working')
    hamMenu.classList.toggle('active')

})

xmark.addEventListener('click', (e) => {
    e.preventDefault()
    console.log('working')
    window.location.href= '/'
})




