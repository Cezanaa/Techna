$(document).ready(function () {
    



    $.ajax({
        url: "/singles-display",
        dataType: "json",
        success: function (result) {
            for (let i = 1; i < result[1] + 1; i++) {
                

                var base64Img = "data:image/jpeg;base64," + result[0][i - 1][2];
                document.getElementById(`single-${i}-img`).src = base64Img;
                document.getElementById(`single-${i}-title`).innerText = result[0][i - 1][0];
                document.getElementById(`single-${i}-date`).innerText = result[0][i - 1][3];
                document.getElementById(`single-${i}`).setAttribute('audio',`data:audio/mp3;base64,` +result[0][i - 1][1]);
                

                
            }
            load_profile_pic();
            load_bio();
        }
    });




    
});

function load_bio(){

    $.ajax({
        url: "/display-bio",
        success: function (result) {
            if (result == "edit your bio in the edit profile section") {
                document.getElementById("artist-bio").innerText = "edit your bio in the edit profile section";
            } else {
                document.getElementById("artist-bio").innerText = result;
            }
        }
    });
}



function load_profile_pic(){

    $.ajax({
        url: "/display-profile-pic",
        success: function (result) {
            
            if(result == "/static/images/default_profile_pic.png"){
                
                document.getElementById("profile-pic").src = result

            }
            else {
                
                var base64Image = "data:image/jpeg;base64," + result;
                document.getElementById("profile-pic").src = base64Image;
                
                
            }
        }
    })



}