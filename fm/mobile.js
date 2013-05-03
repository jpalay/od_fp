$(document).ready(function() {
    // Activate mobile-friendly menu when clicking Sections link.
    $('#masthead-nav-mobile a').click(function() {
        event.preventDefault();
        $('#masthead-nav').toggleClass('mobile-hidden');
        $(this).toggleClass('active');
    });
    $('#magazine-secondary .magazine-mobile-nav a').click(function() {
        event.preventDefault();
        $('#magazine-secondary #magazine-nav').toggleClass('mobile-hidden');
        console.log($('#magazine-secondary #magazine-nav'));
        $(this).toggleClass('active');
    });
    $('#magazine-nav ul li:last-child').click(function() {
        event.preventDefault();
    })
});