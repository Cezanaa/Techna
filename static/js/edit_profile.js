
// prikaze profile pitcure  
     $( document ).ready(function() {
        
        $.ajax({
            url: "/display-profile-pic",
            success: function (result) {
                
                
                if(result == "/static/images/default_profile_pic.png"){
                    
                    document.getElementById("profile-pic").src = result
    
                }
                else {
                    
                    
                    document.getElementById("profile-pic").src = result;
                    
                    
                }
            }
        })

    });
 

