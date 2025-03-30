
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


    const content = document.getElementById('layout-main-content');
    const display = content.style.display
    content.style.display = 'none'; 
    
    RemoveJsCss();
    Promise.all([AppenedJS(jsFile),AppenedCss(cssFile) ])
        .then(()=>{   
            
            
            const contant = document.getElementById('layout-main-content');


            fetch(file)
                .then(response => response.text())
        
                .then(data =>{
                    contant.innerHTML =data;
                    content.style.display = display;
        
                })



        })


}




$( document ).ready(function() {
    Changehtml("home","/static/css/home.css")
});



function play(element){
    var audio = element.getAttribute('audio');
    
    var audio_player = document.getElementById('song-audio');
    audio_player.src = audio;
    audio_player.play();
    console.log("worked")
}


function StopPlay(){
    var audio_player = document.getElementById('song-audio');
    if(audio_player.paused){
        audio_player.play()
    }
    else{
        audio_player.pause()


    }



}


var volume = document.getElementById('volume')
var audio = document.getElementById('song-audio')

volume.addEventListener('input',function(){

    audio.volume = volume.value;

})