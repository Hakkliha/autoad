import {equipment_array} from './equipment_file.js';


let removal_render = () => {
    let picture_list = $("#pictures_pictures").val().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "").split(",");

    let pictrue_editor = "";

    for (let i = 0; i < picture_list.length; i++) {
        pictrue_editor += '<div style="margin-bottom: 10px;" class="picture_remover"><img style="width: 143px; height: 96px; object-fit: cover;" src="../../' + picture_list[i] + '" id="deletable_picture' + i + '" alt="alt"><input type="checkbox" style="margin-left: 15px;" name="picture_remover_box' + i + '" id="picture_remover_box' + i + '"><label style="margin-left: 5px;" for"picture_remover_box' + i + '">Remove</label></div>'
    }

    pictrue_editor = $.parseHTML(pictrue_editor);
    $("#uploaded_pics").html(pictrue_editor);
};


$(document).ready(function () {

    let chosen_equipment = $("#id_equipment").val().split("///");
    for (let i = 0; i < chosen_equipment.length; i++) {
        chosen_equipment[i] = chosen_equipment[i].replace(/(^\s*;)|(;\s*$)/g, '').split(";");
    }
    let equipment_field = $("#equipment_choice_field");
    let equipment_content = "";

    for (let i = 0; i < equipment_array.length; i++) {
        let equipment_internal_content = "";
        for (let j = 1; j < equipment_array[i].length; j++) {
            if (equipment_array[i][0] === "Air conditioning") {
                if (equipment_array[i][j] === chosen_equipment[i][1]) {
                    equipment_internal_content += '<input checked type="radio" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
                } else {
                    equipment_internal_content += '<input type="radio" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
                }
            } else if ((equipment_array[i][0] === "Interior features") || (equipment_array[i][0] === "Safety and Security") || (equipment_array[i][0] === "Wheels and tires") || (equipment_array[i][0] === "Emergency equipment") || (equipment_array[i][0] === "Parking sensors") || (equipment_array[i][0] === "Sport") || (equipment_array[i][0] === "Extras") || (equipment_array[i][0] === "Interior color")) {

                let dont_skip = true;

                for (let x = 1; x < chosen_equipment[i].length; x++) {
                    if (chosen_equipment[i][x] === equipment_array[i][j]) {
                        equipment_internal_content += '<input checked type="checkbox" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
                        dont_skip = false;
                    }
                }
                if (dont_skip) {
                    equipment_internal_content += '<input type="checkbox" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
                }


            } else {
                equipment_internal_content += '<option value="' + equipment_array[i][j] + '">' + equipment_array[i][j] + '</option>';
            }
        }
        if ((equipment_array[i][0] === "Air conditioning") || (equipment_array[i][0] === "Interior features") || (equipment_array[i][0] === "Safety and Security") || (equipment_array[i][0] === "Wheels and tires") || (equipment_array[i][0] === "Emergency equipment") || (equipment_array[i][0] === "Parking sensors") || (equipment_array[i][0] === "Sport") || (equipment_array[i][0] === "Extras") || (equipment_array[i][0] === "Interior color")) {
            equipment_content += '<div class="equipment_selection_field"><h4>' + equipment_array[i][0] + '</h4><div id="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '_field_content">' + equipment_internal_content + '</div></div>';
        } else {
            equipment_content += '<div class="equipment_selection_field"><h4>' + equipment_array[i][0] + '</h4><div id="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '_field_content"><select id="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0] + '">' + equipment_internal_content + '</select></div></div>';
        }
    }

    equipment_content = $.parseHTML(equipment_content);
    equipment_field.html(equipment_content);
    for (let i = 0; i < equipment_array.length; i++) {
        if (equipment_array[i][0] === "Trailer coupling" || equipment_array[i][0] === "Cruise control" || equipment_array[i][0] === "Radio" || equipment_array[i][0] === "Headlights" || equipment_array[i][0] === "Rear lights" || equipment_array[i][0] === "Daytime running lights" || equipment_array[i][0] === "Adaptive lighting" || equipment_array[i][0] === "Airbags") {
            if (chosen_equipment[i].length === 2) {
                $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val(chosen_equipment[i][1]);
            }
        }
    }

    removal_render();


    if ($("#id_is_import").attr('checked')) {
        $(".importaffected").removeClass("d-none");
    }

    if ($("#id_customisation").attr('checked')) {
        $(".customisationaffected").removeClass("d-none");
    }

});


$("#removal_confirmation").click(function () {
    $("#pictures_pictures").val().replace("[", "").replace("]", "").replace(/'/g, "").replace(/ /g, "");
    for (let i = 0; i < $(".picture_remover > input").length; i++) {
        let ischecked = $("#picture_remover_box" + i).is(":checked");//.prev().attr("src");
        if (ischecked) {
            let replaceable_src = $("#picture_remover_box" + i).prev().attr("src");
            let src_removefrom = $("#pictures_pictures").val();
            console.log(replaceable_src);
            let the_output = src_removefrom.replace(replaceable_src.replace("../../", ""), "").replace(/'',/g, "").replace(/, ''/g, "").replace(/ /g, "");
            $("#pictures_pictures").val(the_output);
            console.log($("#pictures_pictures").val());
        }
    }
    removal_render();
});


$("#final_submit").click(function () {
    let e_content = "";
    for (let i = 0; i < equipment_array.length; i++) {
        if (i === 0) {
            e_content += equipment_array[i][0] + ";"
        } else {
            e_content += "///" + equipment_array[i][0] + ";"
        }
        for (let j = 0; j < $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > input").length; j++) {
            let e = $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > input")[j];
            if (e.checked) {
                e_content += $(e).val() + ";";
            }
        }
        if (equipment_array[i][0] === "Trailer coupling" || equipment_array[i][0] === "Cruise control" || equipment_array[i][0] === "Radio" || equipment_array[i][0] === "Headlights" || equipment_array[i][0] === "Rear lights" || equipment_array[i][0] === "Daytime running lights" || equipment_array[i][0] === "Adaptive lighting" || equipment_array[i][0] === "Airbags") {
            if ($("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val() !== "") {
                e_content += $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val();
            }
        }
    }
    $("#id_equipment").val(e_content);
});


$("#vehicle_model").click(function () {
    let modelname = $("#model_fi").val();
    $("#id_model").val(modelname);
});


$("#id_fuel").click(function () {
    let fuel = $("#id_fuel").val();
    if (fuel === 'Electric') {
        if ($(".electicaffected").hasClass("d-none")) {
            $(".fuelaffected").toggleClass("d-none");
            $(".electicaffected").toggleClass("d-none");
        }
    } else {
        if ($(".fuelaffected").hasClass("d-none")) {
            $(".fuelaffected").toggleClass("d-none");
            $(".electicaffected").toggleClass("d-none");
        }
    }
});

$("#id_is_import").change(function () {
    $(".importaffected").toggleClass("d-none");
});

$("#id_customisation").change(function () {
    $(".customisationaffected").toggleClass("d-none");
});