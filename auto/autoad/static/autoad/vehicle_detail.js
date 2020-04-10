$( document ).ready(function () {
	var price = $( "#price_price > b" ).text();
	$( "#price_price > b" ).text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));


	var picture_src = $( "#images_source" ).text().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "").split(",");
	var content = "";
	if (picture_src) {
		for (var i = 0; i < picture_src.length; i++) {
			var src_input = picture_src[i];
			content += '<div><a href="images/"><img src="' + src_input + '" ' + 'class="other_picture_element" id="other_picture' + i + '""></a></div>';
		};
	} else {
		content = '<div><img src="/media/base_media/default/def.jpg" class="other_picture_element"></div>';
	};
	content = $.parseHTML(content);
  	$( "#other_pictures" ).html(content);


  	var equipment_content_array = $( "#equipment_equipment" ).text().split("///");

  	for (var i = 0; i < equipment_content_array.length; i++) {
   	 equipment_content_array[i] = equipment_content_array[i].replace(/(^\s*;)|(;\s*$)/g, '').split(";");
  	};
  	console.log(equipment_content_array);

  	


  	  var equipment_field = $( "#equipment_list_field" );
	  var equipment_content = "";

	for ( var i = 0; i < equipment_content_array.length; i++) {
    	var equipment_internal_content = "";
    	for (var j = 1; j < equipment_content_array[i].length; j++) {
     		equipment_internal_content += "<li>" + equipment_content_array[i][j] + "</li>";
		};
		if (equipment_internal_content != "" && equipment_internal_content != null && equipment_internal_content != undefined) {
			equipment_content += "<div><h3>" + equipment_content_array[i][0] + "</h3><ul>" + equipment_internal_content + "</ul></div>";
		};
	};

  equipment_content = $.parseHTML(equipment_content);
  equipment_field.html(equipment_content);

  $("#other_pictures").slick({
  	arrows: true,
  	dots: true,
  	adaptiveHeight: true
  });
});