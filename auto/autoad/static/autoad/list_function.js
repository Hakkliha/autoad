$(document).ready(function () {
  let brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  let list_name = [];
  let content = "";
  if ((brand !== '') && (brand !== 'OTHER')) {
    list_name = eval(brand + '_MODEL_LIST')
    for (let i = 0; i < list_name.length; i++) {
      content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
    }
  } else {
    content = '<option value="">---------</option>'
  }
  content = $.parseHTML(content);
  $("#vehicle_model").html(content);
  $("#id_vehicle_model").val('');
  for (let i = $(".price_price").length - 1; i >= 0; i--) {
    let price = $(".price_price > b:eq(" + i + ")").text();
    $(".price_price > b:eq(" + i + ")").text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));
  }

  for (let i = $(".mileage").length - 1; i >= 0; i--) {
    let price = $(".mileage > b:eq(" + i + ")").text();
    $(".mileage > b:eq(" + i + ")").text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));
  }

  for (let i = 1; i < $("#list_items > div").length + 1; i++) {
    let img_source = $("#ad_cover" + i).attr('context').replace(/'/g, '').replace(/ /g, '').replace('[', '').replace(']', '').split(',');
    let thumbnail = img_source[0].split("/");
    thumbnail[thumbnail.length - 1] = "thumbnail.jpg";
    thumbnail = thumbnail.join("/");
    if (img_source) {
      $("#ad_cover" + i).attr('src', "../" + thumbnail);
    } else {
      $("#ad_cover" + i).attr('src', '/media/base_media/default/def.jpg');
    }
  }


});

$("#id_brand").click(function () {
  let brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  let list_name = [];
  let content = "---------";
  if ((brand !== '') && (brand !== 'OTHER')) {
    list_name = eval(brand + '_MODEL_LIST')
    for (let i = 0; i < list_name.length; i++) {
      content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
    }
  }
  content = $.parseHTML(content);
  $("#vehicle_model").html(content);
  $("#id_vehicle_model").val('');
});


$("#vehicle_model").click(function () {
  let modelname = $("#vehicle_model").val();
  if ((modelname === 'Any') || (modelname === '')) {
    $("#id_vehicle_model").val('');
  } else {
    $("#id_vehicle_model").val(modelname);
  }
});