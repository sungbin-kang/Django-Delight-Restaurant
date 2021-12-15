$('.menu-bar a').click(function(event){
  event.preventDefault();
  $('.menu-bar a').removeClass('active')
  $(this).addClass('active');
});