import {equipment_array} from './equipment_file.js';

$(document).ready(function () {


    let equipment_field = $("#equipment_choice_field");
    let equipment_content = "";

    for (let i = 0; i < equipment_array.length; i++) {
        let equipment_internal_content = "";
        for (let j = 1; j < equipment_array[i].length; j++) {
            if (equipment_array[i][0] === "Air conditioning") {
                equipment_internal_content += '<input type="radio" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
            } else if ((equipment_array[i][0] === "Interior features") || (equipment_array[i][0] === "Safety and Security") || (equipment_array[i][0] === "Wheels and tires") || (equipment_array[i][0] === "Emergency equipment") || (equipment_array[i][0] === "Parking sensors") || (equipment_array[i][0] === "Sport") || (equipment_array[i][0] === "Extras") || (equipment_array[i][0] === "Interior color")) {
                equipment_internal_content += '<input type="checkbox" style="margin: 0 10px;" value="' + equipment_array[i][j] + '" id="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '" name="' + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><label for="' + equipment_array[i][j].toLowerCase().replace(" ", "_").replace(" ", "_") + '"><h6>' + equipment_array[i][j] + '</h6></label><br>';
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
                e_content += $(e).val() + "; ";
            }

        }

        if (equipment_array[i][0] === "Trailer coupling" || equipment_array[i][0] === "Cruise control" || equipment_array[i][0] === "Radio" || equipment_array[i][0] === "Headlights" || equipment_array[i][0] === "Rear lights" || equipment_array[i][0] === "Daytime running lights" || equipment_array[i][0] === "Adaptive lighting" || equipment_array[i][0] === "Airbags") {
            console.log("CANYON");
            if ($("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val() !== "") {
                e_content += $("#" + equipment_array[i][0].toLowerCase().replace(" ", "_").replace(" ", "_") + "_field_content > select").val();
            }

        }

    }

    $("#id_equipment").val(e_content);
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

$(".average_consumption_field").click(function () {
    let usage_out = parseFloat($("#id_fuel_usage_out").val());
    let usage_city = parseFloat($("#id_fuel_usage_city").val());
    let average_consumption_outuput = (usage_out + usage_city) / 2;
    $(".average_consumption_field").val(average_consumption_outuput);
});

$("#id_is_import").change(function () {
    $(".importaffected").toggleClass("d-none");
});

$("#id_customisation").change(function () {
    $(".customisationaffected").toggleClass("d-none");
});