//prikaze vse "singles" komade
$(document).ready(function () {
    
    $.ajax({
        url: "/singles-display",
        dataType: "json",
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
            load_profile_pic();
            load_bio();
        }
    });




    
});
//prikaze bio
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


// prikaze profile pitcure
function load_profile_pic(){

    $.ajax({
        url: "/display-profile-pic",
        success: function (result) {
            
            
            if(result == "/static/images/default_profile_pic.png"){
                
                document.getElementById("profile-pic").src = result;

            }
            else {
                
                
                document.getElementById("profile-pic").src = result;
                
                
            }
        }
    })



}