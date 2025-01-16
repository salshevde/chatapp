function responsiveWidth(){
    const width = window.innerWidth;
    const style = document.body.style;

    if(width>=992 && width<=1600){
        style.transform = "scale(0.9)";
        style.transformOrigin="top left";
    }
    else if(width>=700 && width<=767){
        style.transform = "scale(0.8)";
        style.transformOrigin="top left";
    }
    else if(width>=600 && width<=70){
        style.transform = "scale(0.75)";
        style.transformOrigin="top left";
    }
    else if(width<=1600){
        style.transform = "scale(0.5)";
        style.transformOrigin="top left";
    }
    else {
        style.transform = "scale(1)";
        style.transformOrigin="top left";
    }
}

function collapseLeftMenu(){
    const leftmenu = document.getElementById('left-menu');
    const container = document.querySelector('.container');
    leftmenu.classList.toggle('collapsed')
    container.classList.toggle('collapsed-menu')
    console.log(leftmenu.classList)
}
function toggleInFilter(){
    const individual = document.querySelector('.filter-chat-btn.in')
    individual.classList.toggle('select-filter')

}
function toggleGrFilter(){
    const group = document.querySelector('.filter-chat-btn.gr')
    group.classList.toggle('select-filter')
}
window.addEventListener('resize',responsiveWidth);
window.addEventListener('load',responsiveWidth);