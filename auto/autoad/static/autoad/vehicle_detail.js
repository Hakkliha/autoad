$(document).ready(function () {
    let price = $("#price_price > b").text();
    $("#price_price > b").text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));


    let picture_src = $("#images_source").text().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "").split(",");
    let content = "";
    if (picture_src) {
        for (let i = 0; i < picture_src.length; i++) {
            let src_input = picture_src[i];
            content += '<div><a href="images/"><img src="../' + src_input + '" ' + 'class="other_picture_element" id="other_picture' + i + '""></a></div>';
        }
    } else {
        content = '<div><img src="/media/base_media/default/def.jpg" class="other_picture_element"></div>';
    }
    content = $.parseHTML(content);
    $("#other_pictures").html(content);


    let equipment_content_array = $("#equipment_equipment").text().split("///");

    for (let i = 0; i < equipment_content_array.length; i++) {
        equipment_content_array[i] = equipment_content_array[i].replace(/(^\s*;)|(;\s*$)/g, '').split(";");
    }
    console.log(equipment_content_array);


    let equipment_field = $("#equipment_list_field");
    let equipment_content = "";

    for (let i = 0; i < equipment_content_array.length; i++) {
        let equipment_internal_content = "";
        for (let j = 1; j < equipment_content_array[i].length; j++) {
            equipment_internal_content += "<li>" + equipment_content_array[i][j] + "</li>";
        }
        if (equipment_internal_content !== "" && equipment_internal_content != null) {
            equipment_content += "<div><h3>" + equipment_content_array[i][0] + "</h3><ul>" + equipment_internal_content + "</ul></div>";
        }
    }

    equipment_content = $.parseHTML(equipment_content);
    equipment_field.html(equipment_content);

    $("#other_pictures").slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true
    });
});