$( document ).ready(function () {


	var picture_src = $( "#images_source" ).text().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "").split(",");
	var content1 = "";
	for (var i = 0; i < picture_src.length; i++) {
		var src_input = picture_src[i];
		content1 += '<div><a href="' + src_input + '"><img src="' + src_input + '" ' + 'class="other_picture_element" id="other_picture' + i + '""></a></div>';
		$( "#other_pictures" )
	};
	content1 = $.parseHTML(content1);
  	$( "#other_pictures" ).html(content1);

  	var content2 = "";
	for (var i = 0; i < picture_src.length; i++) {
		var src_input = picture_src[i];
		content2 += '<div><img src="' + src_input + '" ' + 'class="other_picture_element2" id="other_picture1' + i + '""></div>';
		$( "#other_pictures" )
	};
	content2 = $.parseHTML(content2);

  	$( "#nav_pictures" ).html(content2);

  $("#other_pictures").slick({
  	slidesToShow: 1,
  	slidesToScroll: 1,
  	arrows: false,
  	fade: true,
  	asNavFor: '#nav_pictures'
  });

  $( "#nav_pictures" ).slick({
  	slidesToShow: Math.floor(picture_src.length / 3),
 	  slidesToScroll: 1,
  	asNavFor: '#other_pictures',
  	dots: true,
  	centerMode: true,
  	focusOnSelect: true,
    variableWidth: true
  });

  
});