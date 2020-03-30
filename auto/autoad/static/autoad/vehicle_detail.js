$( document ).ready(function () {
	var price = $( "#price_price" ).text();
	$( "#price_price" ).text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));
	var picture_src = $( "#images_source" ).text().replace("[", "").replace("]", "").split(",");
	console.log(picture_src)
	$( "#main_image" ).attr("src", picture_src[0].replace("\'", "").replace("\'", ""));
	var content = "";
	for (var i = 1; i < picture_src.length; i++) {
		var src_input = picture_src[i].replace("\'", "").replace("\'", "");
		console.log(src_input)
		content += '<img src="' + src_input + '" ' + 'class="other_picture_element" id="other_picture' + i + '"">';
		$( "#other_pictures" )
	};
	content = $.parseHTML(content);
  	$( "#other_pictures" ).html(content);
});