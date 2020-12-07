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
  }) ;
