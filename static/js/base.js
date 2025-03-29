
function AppenedCss(cssFile){
    
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = cssFile;
    link.setAttribute('dinamic',true);
    document.head.appendChild(link);
}

function AppenedJS(jsFile){

    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = jsFile;
    script.setAttribute('dinamic',true);
    document.head.appendChild(script);
}

function RemoveJsCss(){

    const oldCSS = document.querySelector('link[dinamic]');
    if(oldCSS) oldCSS.remove();
    const oldJS = document.querySelector('script[dinamic]');
    if(oldJS) oldJS.remove();
}


function Changehtml(file,cssFile,jsFile){

    
    RemoveJsCss();
    AppenedCss(cssFile);
    AppenedJS(jsFile);
    const contant = document.getElementById('layout-main-content');


    fetch(file)
        .then(response => response.text())

        .then(data =>{
            contant.innerHTML =data;
            
            


        })

}




$( document ).ready(function() {
    Changehtml("home","/static/css/home.css")
});