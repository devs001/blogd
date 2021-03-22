$(document).ready(function() {
$('#like').click(function(){
    $.ajax({
             type: "POST",
             url: "{% url 'artical_m/liked'  %}",
             data: {'jax_id': $(this).attr('name'),'operation':'likeop','csrfmiddlewaretoken': '{{ csrf_token }}'},
             dataType: "json",
             success: function(response) {
 					if(response.like=="login requied") {
 						$('#jax_like').text("login requied")
 					}
                    else if(response.like){
                     $( '#like' ).text("liked")
                    }
                    else{
                      $( '#like' ).text("like it")
                    }
              }
                    });
  })




});


$(document).ready(function() {

var s =     '{{receiver_username}}'.toString();
var url= 'ws://'+window.location.host+'/ws/'+'notifications/';

var chatsocket = new WebSocket(url);

chatsocket.onmessage = function(e){
        var data = JSON.parse(e.data);


        var massage = data.massage;
        var $chat = $('.cha');
        if(massage.type=='notification_massage'){
                var massage_text =massage.massage;
                console.log(massage_text);
            if(massage.sender!='{{request.user.username}}'){
                var massage_target=$('#'+massage.sender+" h2");
                 massage_target.html('<span>'+massage_text+'</span> <span style="background:#dc3545; transform:uppercase;">new</span>');
                 $('#'+massage.sender).css({'background':'#d5c04d'});
                 //$('html, body').animate({scrollTop:massage_target.offset().top},'fast');
                 $('#new').css({'visibility':'visible'});

                 var popup_card=$('.popup');
                 popup_card.html('<p style="font-size:1.3rem; color:white; text-align:center; background-color:#1d3557; "> massage from '+massage.sender+'</p> <p style=" padding-left:.7rem; "> '+massage_text+'</p>');

                 popup_card.toggleClass('active');

                 window.setTimeout(function(){
                    $('.popup').toggleClass('active');}, 2000);
            }
        else{
                $chat.append('<li class="list-unstyled chateli" ><div class="chatbox bubble" style="float:left; background-color:#6c757d; " ><p >'+massage_text+'</p><div class="time">'+ massage.send_time +'</div></div></li></div>');
            }
        }
        else{
        alert("not there");
        $chat.append(' <div class="card card-body border-success  text-right"> <span> Me </span> <span>loading.....</span><h2 class="blockqoute  text-success ">   massage </h2></div>');
        }
        var last=$('.cha li').last().find('.bubble');
        last.animate({'bgcolor':'#fd7e14', 'padding':'+=40px'},'fast');
        last.animate({'bgcolor':'#fd7e14', 'padding':'-=40px'},'slow');


};
chatsocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');

};

        });



        $(document).ready(function () {
            $('#sidebarCollapse').on('click', function () {
                $('#sidebar').toggleClass('active');
            });
        });
