if(typeof jQuery == 'undefined'){
  throws("jq呢????")
}
window.acs = {
  setBlockHeight: function(jqObj){
    //兼容不支持vh的浏览器
    if(jqObj.height() == 0){
      jqObj.css("height",window.innerHeight + "px");
      $(window).resize(function(){
        jqObj.css("height",window.innerHeight + "px");
      })
    }
  },
  setNavBg: function(jqObj){
    if(document.body.scrollTop > (innerHeight-100)){
      jqObj.addClass("navbar-black");
    }
    $(document).scroll(function(){
      if(document.body.scrollTop > (innerHeight-100)){
        jqObj.addClass("navbar-black");
      }else{
        jqObj.removeClass("navbar-black");
      }
    })
  },
  scrollAnchor: function(jqButtoms){
    //for(var jqButtom of jqButtoms){
      jqButtoms.click(function(e){
        e.preventDefault();
        var id = $(this).attr('data-href'),
        top = $(id).offset().top;
        $('html,body').animate({
            'scrollTop':top
        },'slow');
      });
    //}
  }
}

