
// doda css za specificn html page ko se dinamicno zamenja
function AppenedCss(cssFile){
    
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = cssFile;
    link.setAttribute('dinamic',true);
    document.head.appendChild(link);
}

// doda js za specificn html page ko se dinamicno zamenja
function AppenedJS(jsFile){

    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = jsFile;
    script.setAttribute('dinamic',true);
    document.head.appendChild(script);
}
// otstrani js in css prejsne strani
function RemoveJsCss(){

    const oldCSS = document.querySelector('link[dinamic]');
    if(oldCSS) oldCSS.remove();
    const oldJS = document.querySelector('script[dinamic]');
    if(oldJS) oldJS.remove();
}

// dinamicno zamenja html layout-main-content elementa in poklice RemoveJsCss , AppenedJS,AppenedCss
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



// on load prikaze html od home pagea needs work
$( document ).ready(function() {
    Changehtml("home","/static/css/home.css")
});


//on click predvaja komad in prikaze Title,cover,artist v levem spodnjem kotu
function play(element){
    var audio = element.getAttribute('audio');
    var artist =element.getAttribute('Artist');
    var Title = element.getAttribute('Title');
    var Img = element.getAttribute('Img');

    var audio_player = document.getElementById('song-audio');
    audio_player.src = audio;
    audio_player.play();

    document.getElementById('nowPlaying-artist').innerText = artist;
    document.getElementById('nowPlaying-title').innerText = Title;
    document.getElementById('nowPlaying-img').src = Img;


}

//da musko na pauzo ali jo predvaja
function StopPlay(){
    var audio_player = document.getElementById('song-audio');
    if(audio_player.paused){
        audio_player.play()
    }
    else{
        audio_player.pause()


    }



}



//doloca volume muske
volume.addEventListener('input',function(){
    var volume = document.getElementById('volume')
    var audio = document.getElementById('song-audio')
    audio.volume = volume.value;

})
