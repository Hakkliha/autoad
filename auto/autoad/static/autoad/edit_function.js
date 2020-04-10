import {ABARTH_MODEL_LIST, AC_MODEL_LIST, ACURA_MODEL_LIST, AIXAM_MODEL_LIST, ALFAROMEO_MODEL_LIST, ALPINA_MODEL_LIST, ARTEGA_MODEL_LIST, ASIAMOTORS_MODEL_LIST, ASTONMARTIN_MODEL_LIST, AUDI_MODEL_LIST, AUSTIN_MODEL_LIST, AUSTINHEALEY_MODEL_LIST, BENTLEY_MODEL_LIST, BMW_MODEL_LIST, BORGWARD_MODEL_LIST, BRILLIANCE_MODEL_LIST, BUGATTI_MODEL_LIST, BUICK_MODEL_LIST, CADILLAC_MODEL_LIST, CASALINI_MODEL_LIST, CATERHAM_MODEL_LIST, CHATENET_MODEL_LIST, CHEVROLET_MODEL_LIST, CHRYSLER_MODEL_LIST, CITROEN_MODEL_LIST, COBRA_MODEL_LIST, CORVETTE_MODEL_LIST, CUPRA_MODEL_LIST, DACIA_MODEL_LIST, DAEWOO_MODEL_LIST, DAIHATSU_MODEL_LIST, DETOMASO_MODEL_LIST, DODGE_MODEL_LIST, DONKERVOORT_MODEL_LIST, DSAUTOMOBILES_MODEL_LIST, FERRARI_MODEL_LIST, FIAT_MODEL_LIST, FISKER_MODEL_LIST, FORD_MODEL_LIST, GACGONOW_MODEL_LIST, GEMBALLA_MODEL_LIST, GMC_MODEL_LIST, GRECAV_MODEL_LIST, HAMANN_MODEL_LIST, HOLDEN_MODEL_LIST, HONDA_MODEL_LIST, HUMMER_MODEL_LIST, HYUNDAI_MODEL_LIST, INFINITI_MODEL_LIST, ISUZU_MODEL_LIST, IVECO_MODEL_LIST, JAGUAR_MODEL_LIST, JEEP_MODEL_LIST, KIA_MODEL_LIST, KOENIGSEGG_MODEL_LIST, KTM_MODEL_LIST, LADA_MODEL_LIST, LAMBORGHINI_MODEL_LIST, LANCIA_MODEL_LIST, LANDROVER_MODEL_LIST, LANDWIND_MODEL_LIST, LEXUS_MODEL_LIST, LIGIER_MODEL_LIST, LINCOLN_MODEL_LIST, LOTUS_MODEL_LIST, MAHINDRA_MODEL_LIST, MASERATI_MODEL_LIST, MAYBACH_MODEL_LIST, MAZDA_MODEL_LIST, MCLAREN_MODEL_LIST, MERCEDES_BENZ_MODEL_LIST, MG_MODEL_LIST, MICROCAR_MODEL_LIST, MINI_MODEL_LIST, MITSUBISHI_MODEL_LIST, MORGAN_MODEL_LIST, NISSAN_MODEL_LIST, NSU_MODEL_LIST, OLDSMOBILE_MODEL_LIST, OPEL_MODEL_LIST, PAGANI_MODEL_LIST, PEUGEOT_MODEL_LIST, PIAGGIO_MODEL_LIST, PLYMOUTH_MODEL_LIST, POLESTAR_MODEL_LIST, PONTIAC_MODEL_LIST, PORSCHE_MODEL_LIST, PROTON_MODEL_LIST, RENAULT_MODEL_LIST, ROLLS_ROYCE_MODEL_LIST, ROVER_MODEL_LIST, RUF_MODEL_LIST, SAAB_MODEL_LIST, SANTANA_MODEL_LIST, SEAT_MODEL_LIST, SKODA_MODEL_LIST, SMART_MODEL_LIST, SPEEDART_MODEL_LIST, SPYKER_MODEL_LIST, SSANGYONG_MODEL_LIST, SUBARU_MODEL_LIST, SUZUKI_MODEL_LIST, TALBOT_MODEL_LIST, TATA_MODEL_LIST, TECHART_MODEL_LIST, TESLA_MODEL_LIST, TOYOTA_MODEL_LIST, TRABANT_MODEL_LIST, TRIUMPH_MODEL_LIST, TVR_MODEL_LIST, VOLKSWAGEN_MODEL_LIST, VOLVO_MODEL_LIST, WARTBURG_MODEL_LIST, WESTFIELD_MODEL_LIST, WIESMANN_MODEL_LIST} from './model_list_file.js';
import {equipment_array} from './equipment_file.js';


 var removal_render = () => {
    var picture_list = $( "#pictures_pictures" ).val().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "").split(",");

    var pictrue_editor = "";

    for (var i = 0; i < picture_list.length; i++) {
      pictrue_editor += '<div style="margin-bottom: 10px;" class="picture_remover"><img style="width: 143px; height: 96px; object-fit: cover;" src="' + picture_list[i] + '" id="deletable_picture' + i + '"><input type="checkbox" style="margin-left: 15px;" name="picture_remover_box' + i + '" id="picture_remover_box' + i + '"><label style="margin-left: 5px;" for"picture_remover_box' + i + '">Remove</label></div>'
    };

    pictrue_editor = $.parseHTML(pictrue_editor);
    $( "#uploaded_pics" ).html(pictrue_editor);
  };




$( document ).ready(function () {
  var brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  var list_name = eval(brand + '_MODEL_LIST');
  var model_content = "";


  for (var i = 1; i < list_name.length; i++){
    model_content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
  };
  model_content = $.parseHTML(model_content);
  $( "#vehicle_model" ).html(model_content);
  if ($( "#id_vehicle_model" ).val() != "") {
    $( "#vehicle_model" ).val($( "#id_vehicle_model" ).val()); 
  };

  var chosen_equipment = $( "#id_equipment" ).val().split("///");
  for (var i = 0; i < chosen_equipment.length; i++) {
    chosen_equipment[i] = chosen_equipment[i].replace(/(^\s*;)|(;\s*$)/g, '').split(";");
  };
  var equipment_field = $( "#equipment_choice_field" );
  var equipment_content = "";

   for ( var i = 0; i < equipment_array.length; i++) {
    var equipment_internal_content = "";
    for (var j = 1; j < equipment_array[i].length; j++) {
      if (equipment_array[i][0] == "Air conditioning") {
        if (equipment_array[i][j] == chosen_equipment[i][1]) {
        equipment_internal_content += '<input checked type="radio" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
        } else {
        equipment_internal_content += '<input type="radio" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
      };
    } else if ((equipment_array[i][0] == "Interior features") || (equipment_array[i][0] == "Safety and Security") || (equipment_array[i][0] == "Wheels and tires") || (equipment_array[i][0] == "Emergency equipment") || (equipment_array[i][0] == "Parking sensors") || (equipment_array[i][0] == "Sport") || (equipment_array[i][0] == "Extras") || (equipment_array[i][0] == "Interior color")) {
    
    var dont_skip = true;

    for (var x = 1; x < chosen_equipment[i].length; x++) {
      if (chosen_equipment[i][x] == equipment_array[i][j]) {
        equipment_internal_content += '<input checked type="checkbox" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
        dont_skip = false;
    };
  };
    if (dont_skip) {
    equipment_internal_content += '<input type="checkbox" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
   };


    } else {
      equipment_internal_content += '<option value="' + equipment_array[i][j] + '">' + equipment_array[i][j] + '</option>';
    };
  };
  if ((equipment_array[i][0] == "Air conditioning") || (equipment_array[i][0] == "Interior features") || (equipment_array[i][0] == "Safety and Security")|| (equipment_array[i][0] == "Wheels and tires") || (equipment_array[i][0] == "Emergency equipment") || (equipment_array[i][0] == "Parking sensors") || (equipment_array[i][0] == "Sport") || (equipment_array[i][0] == "Extras") || (equipment_array[i][0] == "Interior color")) {
    equipment_content += '<div class="equipment_selection_field"><h4>' + equipment_array[i][0] + '</h4><div id="'+ equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") +'_field_content">' + equipment_internal_content + '</div></div>';
  } else {
    equipment_content += '<div class="equipment_selection_field"><h4>' + equipment_array[i][0] + '</h4><div id="'+ equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") +'_field_content"><select id="'+ equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_")  +'" name="'+ equipment_array[i][0] +'">' + equipment_internal_content + '</select></div></div>';
  };
};

  equipment_content = $.parseHTML(equipment_content);
  equipment_field.html(equipment_content);
  for (var i = 0; i < equipment_array.length; i++) {
    if (equipment_array[i][0] == "Trailer coupling" || equipment_array[i][0] == "Cruise control" || equipment_array[i][0] == "Radio" || equipment_array[i][0] == "Headlights" || equipment_array[i][0] == "Rear lights" || equipment_array[i][0] == "Daytime running lights" || equipment_array[i][0] == "Adaptive lighting" || equipment_array[i][0] == "Airbags") {
      if (chosen_equipment[i].length == 2) {
         $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val(chosen_equipment[i][1]);
      };
    };
  };

  removal_render();



    if ($( "#id_is_import" ).attr('checked')) {
    var importaffected = $( ".importaffected" ).removeClass("d-none");
  };

   if ($( "#id_customisation" ).attr('checked')) {
    var customisationaffected = $( ".customisationaffected" ).removeClass("d-none");
  };
});



$( "#removal_confirmation" ).click(function(){
  var picture_list = $( "#pictures_pictures" ).val().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "");
  var checked_boxes = "";
  for (var i = 0; i < $( ".picture_remover > input" ).length; i++) {
    var ischecked = $( "#picture_remover_box" + i ).is(":checked");//.prev().attr("src");
    if (ischecked) {
      var replaceable_src = $( "#picture_remover_box" + i ).prev().attr("src");
      var src_removefrom = $( "#pictures_pictures" ).val();
      console.log(replaceable_src);
      var the_output = src_removefrom.replace(replaceable_src, "").replace(/'',/g, "").replace(/, ''/g, "").replace(/ /g, "");
      $( "#pictures_pictures" ).val(the_output);
      console.log($( "#pictures_pictures" ).val());
    };
  };
  removal_render();
});






$( "#final_submit" ).click(function () {
   var e_content = "";
  for (var i = 0; i < equipment_array.length; i++) {
    if (i == 0) {
      e_content += equipment_array[i][0] + ";"
    } else {
      e_content += "///" + equipment_array[i][0] + ";"
    };
    for (var j = 0; j < $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > input").length; j++) {
     var e = $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > input")[j];
     if (e.checked) {     
      e_content += $(e).val() + ";";
     };
    };
    if (equipment_array[i][0] == "Trailer coupling" || equipment_array[i][0] == "Cruise control" || equipment_array[i][0] == "Radio" || equipment_array[i][0] == "Headlights" || equipment_array[i][0] == "Rear lights" || equipment_array[i][0] == "Daytime running lights" || equipment_array[i][0] == "Adaptive lighting" || equipment_array[i][0] == "Airbags") {
      if ($("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val() != "") {
        e_content += $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val();
      };
    };
  };
  $( "#id_equipment" ).val(e_content);
});


$( "#id_brand" ).click(function() {
  var brand = $("#id_brand").val().toUpperCase().replace(' ', '').replace('-', '_');
  var list_name = eval(brand + '_MODEL_LIST');
  var model_content = "";
  for (var i = 1; i < list_name.length; i++){
    model_content += '<option value="' + list_name[i] + '">' + list_name[i] + '</option>'
  };
  model_content = $.parseHTML(model_content);
  $( "#vehicle_model" ).html(model_content);
});

$( "#vehicle_model" ).click(function() {
  var modelname = $( "#vehicle_model" ).val();
  $( "#id_vehicle_model" ).val(modelname);
});

$( "#id_vehicle_type" ).click(function() {
  var vehicle_type = $("#id_vehicle_type").val();
});

$( "#id_fuel" ).click(function() {
  var fuel = $("#id_fuel").val();
  if (fuel == 'Electric') {
    if ($(".electicaffected").hasClass("d-none")){
      $(".fuelaffected").toggleClass("d-none");
      $(".electicaffected").toggleClass("d-none");
    };
  } else {
    if ($(".fuelaffected").hasClass("d-none")){
      $(".fuelaffected").toggleClass("d-none");
      $(".electicaffected").toggleClass("d-none");
    };
  };
});

$( "#id_is_import" ).change(function () {
  var importaffected = $( ".importaffected" ).toggleClass("d-none");
});

$( "#id_customisation" ).change(function () {
  var customisationaffected = $( ".customisationaffected" ).toggleClass("d-none");
});