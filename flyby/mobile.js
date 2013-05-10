$(document).ready(function() {
	// Activate mobile-friendly menu when clicking Sections link.
	$('#masthead-nav-mobile a').click(function() {
		event.preventDefault();
		$('#masthead-nav').toggleClass('mobile-hidden');
		$(this).toggleClass('active');
	});
    $('#blog-small-nav a').click(function() {
        event.preventDefault();
        $('#blog-nav').toggleClass('small-hidden');
        $(this).toggleClass('active');
    });
});