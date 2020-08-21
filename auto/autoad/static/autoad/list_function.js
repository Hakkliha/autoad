import { ABARTH_MODEL_LIST, AC_MODEL_LIST, ACURA_MODEL_LIST, AIXAM_MODEL_LIST, ALFAROMEO_MODEL_LIST, ALPINA_MODEL_LIST, ARTEGA_MODEL_LIST, ASIAMOTORS_MODEL_LIST, ASTONMARTIN_MODEL_LIST, AUDI_MODEL_LIST, AUSTIN_MODEL_LIST, AUSTINHEALEY_MODEL_LIST, BENTLEY_MODEL_LIST, BMW_MODEL_LIST, BORGWARD_MODEL_LIST, BRILLIANCE_MODEL_LIST, BUGATTI_MODEL_LIST, BUICK_MODEL_LIST, CADILLAC_MODEL_LIST, CASALINI_MODEL_LIST, CATERHAM_MODEL_LIST, CHATENET_MODEL_LIST, CHEVROLET_MODEL_LIST, CHRYSLER_MODEL_LIST, CITROEN_MODEL_LIST, COBRA_MODEL_LIST, CORVETTE_MODEL_LIST, CUPRA_MODEL_LIST, DACIA_MODEL_LIST, DAEWOO_MODEL_LIST, DAIHATSU_MODEL_LIST, DETOMASO_MODEL_LIST, DODGE_MODEL_LIST, DONKERVOORT_MODEL_LIST, DSAUTOMOBILES_MODEL_LIST, FERRARI_MODEL_LIST, FIAT_MODEL_LIST, FISKER_MODEL_LIST, FORD_MODEL_LIST, GACGONOW_MODEL_LIST, GEMBALLA_MODEL_LIST, GMC_MODEL_LIST, GRECAV_MODEL_LIST, HAMANN_MODEL_LIST, HOLDEN_MODEL_LIST, HONDA_MODEL_LIST, HUMMER_MODEL_LIST, HYUNDAI_MODEL_LIST, INFINITI_MODEL_LIST, ISUZU_MODEL_LIST, IVECO_MODEL_LIST, JAGUAR_MODEL_LIST, JEEP_MODEL_LIST, KIA_MODEL_LIST, KOENIGSEGG_MODEL_LIST, KTM_MODEL_LIST, LADA_MODEL_LIST, LAMBORGHINI_MODEL_LIST, LANCIA_MODEL_LIST, LANDROVER_MODEL_LIST, LANDWIND_MODEL_LIST, LEXUS_MODEL_LIST, LIGIER_MODEL_LIST, LINCOLN_MODEL_LIST, LOTUS_MODEL_LIST, MAHINDRA_MODEL_LIST, MASERATI_MODEL_LIST, MAYBACH_MODEL_LIST, MAZDA_MODEL_LIST, MCLAREN_MODEL_LIST, MERCEDES_BENZ_MODEL_LIST, MG_MODEL_LIST, MICROCAR_MODEL_LIST, MINI_MODEL_LIST, MITSUBISHI_MODEL_LIST, MORGAN_MODEL_LIST, NISSAN_MODEL_LIST, NSU_MODEL_LIST, OLDSMOBILE_MODEL_LIST, OPEL_MODEL_LIST, PAGANI_MODEL_LIST, PEUGEOT_MODEL_LIST, PIAGGIO_MODEL_LIST, PLYMOUTH_MODEL_LIST, POLESTAR_MODEL_LIST, PONTIAC_MODEL_LIST, PORSCHE_MODEL_LIST, PROTON_MODEL_LIST, RENAULT_MODEL_LIST, ROLLS_ROYCE_MODEL_LIST, ROVER_MODEL_LIST, RUF_MODEL_LIST, SAAB_MODEL_LIST, SANTANA_MODEL_LIST, SEAT_MODEL_LIST, SKODA_MODEL_LIST, SMART_MODEL_LIST, SPEEDART_MODEL_LIST, SPYKER_MODEL_LIST, SSANGYONG_MODEL_LIST, SUBARU_MODEL_LIST, SUZUKI_MODEL_LIST, TALBOT_MODEL_LIST, TATA_MODEL_LIST, TECHART_MODEL_LIST, TESLA_MODEL_LIST, TOYOTA_MODEL_LIST, TRABANT_MODEL_LIST, TRIUMPH_MODEL_LIST, TVR_MODEL_LIST, VOLKSWAGEN_MODEL_LIST, VOLVO_MODEL_LIST, WARTBURG_MODEL_LIST, WESTFIELD_MODEL_LIST, WIESMANN_MODEL_LIST } from './model_list_file.js';

$(document).ready(function () {
  var brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  var list_name = [];
  var content = "";
  if ((brand != '') && (brand != 'OTHER')) {
    list_name = eval(brand + '_MODEL_LIST')
    for (var i = 0; i < list_name.length; i++) {
      content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
    };
  } else {
    content = '<option value="">---------</option>'
  };
  content = $.parseHTML(content);
  $("#vehicle_model").html(content);
  $("#id_vehicle_model").val('');
  for (var i = $(".price_price").length - 1; i >= 0; i--) {
    var price = $(".price_price > b:eq(" + i + ")").text();
    $(".price_price > b:eq(" + i + ")").text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));
  };

  for (var i = $(".mileage").length - 1; i >= 0; i--) {
    var price = $(".mileage > b:eq(" + i + ")").text();
    $(".mileage > b:eq(" + i + ")").text(price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "));
  };

  for (var i = 1; i < $("#list_items > div").length + 1; i++) {
    var img_source = $("#ad_cover" + i).attr('context').replace(/'/g, '').replace(/ /g, '').replace('[', '').replace(']', '').split(',');
    var thumbnail = img_source[0].split("/");
    thumbnail[thumbnail.length - 1] = "thumbnail.jpg";
    thumbnail = thumbnail.join("/");
    if (img_source) {
      $("#ad_cover" + i).attr('src', "../" + thumbnail);
    } else {
      $("#ad_cover" + i).attr('src', '/media/base_media/default/def.jpg');
    };
  };


});

$("#id_brand").click(function () {
  var brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  var list_name = [];
  var content = "---------";
  if ((brand != '') && (brand != 'OTHER')) {
    list_name = eval(brand + '_MODEL_LIST')
    for (var i = 0; i < list_name.length; i++) {
      content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
    };
  };
  content = $.parseHTML(content);
  $("#vehicle_model").html(content);
  $("#id_vehicle_model").val('');
});


$("#vehicle_model").click(function () {
  var modelname = $("#vehicle_model").val();
  if ((modelname == 'Any') || (modelname == '')) {
    $("#id_vehicle_model").val('');
  } else {
    $("#id_vehicle_model").val(modelname);
  };
});