$(document).ready(function () {
    
    $.ajax({
        url: "/display-profile-pic",
        success: function (result) {
            if (result == "static/default_profile_pic.png") {
                document.getElementById("profile-pic").src = result;
            } else {
                var base64Image = "data:image/jpeg;base64," + result;
                document.getElementById("profile-pic").src = base64Image;
            }
        }
    });


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


    $.ajax({
        url: "/singles-display",
        dataType: "json",
        success: function (result) {
            for (let i = 1; i < result[1] + 1; i++) {
                console.log(result[0][i - 1][1]);

                var base64Img = "data:image/jpeg;base64," + result[0][i - 1][2];
                document.getElementById(`single-${i}-img`).src = base64Img;
                document.getElementById(`single-${i}-title`).innerText = result[0][i - 1][0];
                document.getElementById(`single-${i}-date`).innerText = result[0][i - 1][3];
            }
        }
    });
});


