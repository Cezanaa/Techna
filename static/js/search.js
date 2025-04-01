$(document).ready(function () {
    const search = document.getElementById("search");
    console.log(search)

});



search.addEventListener('keyup',(e)=>{
    
    const value = document.getElementById('search').value;
    
    
        $.ajax({
            url: "/search",
            type: "POST",
            contentType: "text/plain",
            data: value,
            success: function (result) {
                
                console.log("test");
                console.log(result);

            }
        });

        
        $.ajax({
            url: "songs-display-search",
            dataType: "json",
            data: value,
            success: function (result) {
                
                for (let i = 1; i < result[1] + 1; i++) {
                    
    
                    
                    document.getElementById(`single-${i}-img`).src = result[0][i - 1][2];
                    document.getElementById(`single-${i}-title`).innerText = result[0][i - 1][0];
                    document.getElementById(`single-${i}-date`).innerText = result[0][i - 1][3];
    
                    document.getElementById(`single-${i}`).setAttribute('audio',result[0][i - 1][1]);
                    document.getElementById(`single-${i}`).setAttribute('Artist',result[0][i - 1][4]);
                    document.getElementById(`single-${i}`).setAttribute('Title',result[0][i - 1][0]);
                    document.getElementById(`single-${i}`).setAttribute('Img',result[0][i - 1][2]);                
    
                    
                }

            }
        });
    
    
    
    
        
    
    
    
        
        $.ajax({
            url: "/artist-display-search",
            dataType: "json",
            data: value,
            success: function (result) {
                
                for (let i = 1; i < result[1] + 1; i++) {
                    
    
                    
                    document.getElementById(`single-${i}-img`).src = result[0][i - 1][2];
                    document.getElementById(`single-${i}-name`).innerText = result[0][i - 1][0];
                    document.getElementById(`single-${i}-followers`).innerText = result[0][i - 1][1];
    
              
    
                    
                }

            }
        });
    
    
    
    
        
    


});

