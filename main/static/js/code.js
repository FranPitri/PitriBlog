$(function(){
    
    $container = $('.articles-container');
    $pagination = $('.pagination');
    $nav = $('.nav');
    
    toggleNav()
    
    $.scrollify({
        section: "section",
        scrollSpeed: 800,
        after: toggleNav,
    })
    
    //Change each article color, checking their postid
    $container.children().each(function(){
        if ( ((parseInt($(this).attr("data-postid")) + 1 ) % 2) == 0 ){
            $(this).css("background-color","#f5f5f5");
        } else {
            $(this).css("background-color","#f9f9f9");
        }
    });
    
    $pagination.css("background-color", $('.articles-container').find(".article").last().css("background-color"));
    
    function checkSection(){
        return window.location.href.split('#')[window.location.href.split('#').length - 1];
    }
    
    function toggleNav(){
        if ( checkSection() != 'articles'){
            $nav.fadeOut(500);
        } else {
            $nav.fadeIn(500);
        }
    }
    
});