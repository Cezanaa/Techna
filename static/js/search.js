

setTimeout(() => {
document.getElementById("search").addEventListener('keyup',(e)=>{

    var search = document.getElementById("search")
    const value = search.value;
    
    const ul = document.getElementById("display");
    ul.innerHTML = "";
    
    
    if(!value){
        value = "aidjaifjhgfiaoidakdkjaijqijqijfqpiodqoi12ou921ure92juo9jurq989frq0rfqo09q'9ujq"
    }
       
    $.ajax({
        url: `songs-display-search?search=${encodeURIComponent(value)}`,
        dataType: "json",
        
        success: function (result) {

                
                
            for (let i = 1; i < result[1] + 1; i++) {

                    
                    
                    
                const item = document.createElement("li");
                item.id = `song-${i}-ls`;  
                document.getElementById("display").appendChild(item);

                const song_container = document.createElement("div");
                song_container.id = `song-${i}-div`;
                song_container.className = `song-div`;
                document.getElementById(item.id).appendChild(song_container);
                    
                

                document.getElementById(`song-${i}-div`).setAttribute('audio',result[0][i - 1][1]);
                document.getElementById(`song-${i}-div`).setAttribute('Artist',result[0][i - 1][4]);
                document.getElementById(`song-${i}-div`).setAttribute('Title',result[0][i - 1][0]);
                document.getElementById(`song-${i}-div`).setAttribute('Img',result[0][i - 1][2]);
                song_container.onclick = ()=>{play(song_container)};

                 // Create image container
                const imgContainer = document.createElement("div");
                imgContainer.className = "img-container";
                song_container.appendChild(imgContainer);

                
                const img = document.createElement("img");
                imgContainer.appendChild(img);
                img.src = result[0][i - 1][2];
                img.className = `img`
                    
                const contentContainer = document.createElement("div");
                contentContainer.className = "content-container"; // Add a class for styling
                contentContainer.id = `text-${i}-div`;
                song_container.appendChild(contentContainer);

                    
                const title = document.createElement("p");
                contentContainer.appendChild(title);
                title.innerText = result[0][i - 1][0];
                title.className = `title`
                    
                const artist = document.createElement("p");
                contentContainer.appendChild(artist);
                artist.innerText = result[0][i - 1][4];
                artist.className = `artist`


                const streams = document.createElement("p");
                contentContainer.appendChild(streams);
                streams.innerText = result[0][i - 1][5] + " plays";
                streams.className = `streams`
                    


                
                    


                    
                }

            }
        });
    
        $.ajax({
            url: `artist-display-search?search=${encodeURIComponent(value)}`,
            dataType: "json",
            
            success: function (result) {
    
                    
                    
                for (let i = 1; i < result[1] + 1; i++) {
    
                        
                        
                        
                    const item = document.createElement("li");
                    item.id = `artist-${i}-ls`;  
                    document.getElementById("display").appendChild(item);
    
                    const artist_container = document.createElement("div");
                    artist_container.id = `artist-${i}-div`;
                    artist_container.className = `aertist-div`;
                    document.getElementById(item.id).appendChild(artist_container);
                        
                    
    
    
                     // Create image container
                    const imgContainer = document.createElement("div");
                    imgContainer.className = "img-container";
                    artist_container.appendChild(imgContainer);
    
                    
                    const img = document.createElement("img");
                    imgContainer.appendChild(img);
                    img.src = result[0][i - 1][2];
                    img.className = `img-artist`
                        
                    const contentContainer = document.createElement("div");
                    contentContainer.className = "content-container"; 
                    contentContainer.id = `text-${i}-div`;
                    artist_container.appendChild(contentContainer);
    
                        
                    const artist = document.createElement("p");
                    contentContainer.appendChild(artist);
                    artist.innerText = result[0][i - 1][0];
                    artist.className = `artist`
                        
    
    
                    const followers = document.createElement("p");
                    contentContainer.appendChild(followers);
                    followers.innerText = result[0][i - 1][1] + " followers";
                    followers.className = `followers`
                        
    
    
                    
                        
    
    
                        
                    }
    
                }
        });
    
           
    


});


   
}, 200);