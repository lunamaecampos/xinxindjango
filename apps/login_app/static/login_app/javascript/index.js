$(function(){
  var documentEl = $(document),
      fadeElem = $("#landingwrapper");
  documentEl.on('scroll', function(){
    var currScrollPos = documentEl.scrollTop();

    fadeElem.each(function(){
      var $this = $(this),
        elemOffsetTop = $this.offset().top;
      if(currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/200);
    });
  });
});
$(function(){
  var documentEl = $(document),
      fadeElem = $("#video");
  documentEl.on('scroll', function(){
    var currScrollPos = documentEl.scrollTop();

    fadeElem.each(function(){
      var $this = $(this),
        elemOffsetTop = $this.offset().top;
      if(currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/200);
    });
  });
});
$(function(){
  var documentEl = $(document),
      fadeElem = $("#mobilebandcampplayer");
  documentEl.on('scroll', function(){
    var currScrollPos = documentEl.scrollTop();

    fadeElem.each(function(){
      var $this = $(this),
        elemOffsetTop = $this.offset().top;
      if(currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/150);
    });
  });
});
$(function(){
  var documentEl = $(document),
      fadeElem = $("#bandcampplayer");
  documentEl.on('scroll', function(){
    var currScrollPos = documentEl.scrollTop();

    fadeElem.each(function(){
      var $this = $(this),
        elemOffsetTop = $this.offset().top;
      if(currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/300);
    });
  });
});
$(function(){
  var documentEl = $(document),
      fadeElem = $("#formcontainer");
  documentEl.on('scroll', function(){
    var currScrollPos = documentEl.scrollTop();

    fadeElem.each(function(){
      var $this = $(this),
        elemOffsetTop = $this.offset().top;
      if(currScrollPos > elemOffsetTop) $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/300);
    });
  });
});
