let dropDown = document.getElementsByClassName('dropdown');


dropDown[0].addEventListener('mouseover', event =>{
    document.body.style.backgroundColor='red';
});
dropDown[0].addEventListener('mouseout', event =>{
    document.body.style.backgroundColor='white';
})
