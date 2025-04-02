


search.addEventListener('keyup',(e)=>{



    const value = document.getElementById('search').value;
    console.log(value)
    
    

        
        $.ajax({
            url: "songs-display-search",
            dataType: "json",
            data: value,
            success: function (result) {

                
                
                for (let i = 1; i < result[1] + 1; i++) {

                    
                    
                    
                    const item = document.createElement("li");
                    item.id = `song-${i}`;
                    console.log("test")
                    
                    document.getElementById("display").appendChild(item);
                    
                    console.log("test2")
                    document.getElementById(`song-${i}`).setAttribute('audio',result[0][i - 1][1]);
                    document.getElementById(`song-${i}`).setAttribute('Artist',result[0][i - 1][4]);
                    document.getElementById(`song-${i}`).setAttribute('Title',result[0][i - 1][0]);
                    document.getElementById(`song-${i}`).setAttribute('Img',result[0][i - 1][2]);

                    document.getElementById("test3")
                    const img = document.createElement(img);
                    document.getElementById(item.id).appendChild(img);
                    img.src = result[0][i - 1][2];
                    


                    
                    const title = document.createElement(p);
                    document.getElementById(item.id).appendChild(title);
                    title.innerText = result[0][i - 1][0];
                    

                    const date = document.createElement(p);
                    document.getElementById(item.id).appendChild(date);
                    date.innerText = result[0][i - 1][3];


                    const streams = document.createElement(p);
                    document.getElementById(item.id).appendChild(streams);
                    streams.innerText = result[0][i - 1][5];
                    

                    const artist = document.createElement(p);
                    document.getElementById(item.id).appendChild(artist);
                    artist.innerText = result[0][i - 1][4];
                    

                    /*
                    document.getElementById(`single-${i}-img`).src = result[0][i - 1][2];
                    document.getElementById(`single-${i}-title`).innerText = result[0][i - 1][0];
                    document.getElementById(`single-${i}-date`).innerText = result[0][i - 1][3];
    
                    document.getElementById(`single-${i}`).setAttribute('audio',result[0][i - 1][1]);
                    document.getElementById(`single-${i}`).setAttribute('Artist',result[0][i - 1][4]);
                    document.getElementById(`single-${i}`).setAttribute('Title',result[0][i - 1][0]);
                    document.getElementById(`single-${i}`).setAttribute('Img',result[0][i - 1][2]);                
                    */
                    
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

