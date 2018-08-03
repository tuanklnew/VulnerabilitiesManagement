var rowIDSelected = null;
$(document).ready(
    //
    // Decleare vulnerability table
    //
    $(function () {
        $("#vulntable").bootstrapTable({
            columns:[
                {
                    field: 'state',
                    checkbox: true,
                    align: 'center',
                    valign: 'middle'
                },
                {
                    title: "Vulnerability",
                    field: "name",
                    align: "center",
                    valign: "middle",
                    formatter: HrefFormater,
                    sortable: true
                },
                {
                    title: "Level Risk",
                    field: "levelRisk",
                    align: "center",
                    valign: "middle",
                    sortable: true
                },
                {
                    title: "CVE",
                    field: "cve",
                    align: "center",
                    valign: "middle",
                    sortable: true
                },
                {
                    title: "Service",
                    field: "service.name",
                    align: "center",
                    valign: "middle",
                    sortable: true
                },
                {
                    title: "Description",
                    field: "description",
                    align: "center",
                    valign: "middle",
                    sortable: true
                }
            ],
            url: "/vuln/api/getvulns",
            method: "get",
            idField: "id",
            queryParamsType: "",
            striped: true,
            pagination: true,
            sidePagination: "server",
            pageList: [5, 10, 20, 50, 100, 200, 'All'],
            search: true,
        })
    }),


    //
    // Edit vuln
    //
    $("#editVulnPostForm").submit(function(e){
        var data = $('#editVulnPostForm').serializeArray();
        data.push({name: "id", value: rowIDSelected});
        data = $.param(data);
        $.post("./api/updatevuln", data, function(data){
            var notification = $("#retMsgEdit");
            var closebtn = '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>';
            notification.removeClass("hidden");
            if(data.status != 0){
                notification.html("Error: "+data.message + '. '+data.detail.name[0]);
                notification.removeClass("alert-info");
                notification.addClass("alert-danger");
            }
            else{
                notification.html("The vulnerability is edited.");
                notification.removeClass("alert-danger");
                notification.addClass("alert-info");
            }
            notification.append(closebtn);
            $("#vulntable").bootstrapTable('refresh');
        });
        e.preventDefault();
    }),
    $("#editVulnModal").on("hidden.bs.modal", function () {
        $("#retMsgEdit").addClass("hidden");
    }),

    //
    // Add New vuln
    //
    $("#addVulnPostForm").submit(function(e){
        $.post("./api/addvuln", $(this).serialize(), function(data){
            var notification = $("#retMsgAdd");
            var closebtn = '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button>';
            notification.removeClass("hidden");
            if(data.status != 0){
                notification.html("Error: "+data.message + '. '+data.detail.name[0]);
                notification.removeClass("alert-info");
                notification.addClass("alert-danger");
            }
            else{
                notification.html("New vulnerability is added.");
                notification.removeClass("alert-danger");
                notification.addClass("alert-info");
            }
            notification.append(closebtn);
            $("#vulntable").bootstrapTable('refresh');
        });
        e.preventDefault();
    }),
    $("#addVulnModal").on("hidden.bs.modal", function () {
        $("#retMsgAdd").addClass("hidden");
    }),

    //
    // Confirm delete vuln
    //
    $("#confirmDelete").click(function () {
        // Get csrf_token
        var csrf_token = $('meta[name="csrf-token"]').attr('content');

        // Create array contains vuln ids
        var dataTable = $("#vulntable").bootstrapTable('getSelections');
            var ids = new Array();
            for(i=0; i < dataTable.length; i++){
                ids.push(dataTable[i].id);
            }
        // Create array
        var data = [];
        data.push({name: "id", value: ids});
        data.push({name: "csrfmiddlewaretoken", value: csrf_token});
        $.post('./api/deletevuln', $.param(data),
             function(returnedData){
                if(returnedData.status == 0){
                    $('#warningOnDelete').modal('hide');
                    $("#vulntable").bootstrapTable('refresh');
                }
        }, 'json');
        $('#warningOnDelete').modal('hide')
    }),

    //
    // show delete vuln warning
    //
    $("#delete").click(function () {
        var data = $("#vulntable").bootstrapTable('getSelections');
        if(data.length > 0){
            if(data.length == 1){
                $('#msgOnDelete').text("Are you sure to delete " + data.length + " selected vulnerability?");
            }
            else{
                $('#msgOnDelete').text("Are you sure to delete " + data.length + " selected vulnerabilities?");
            }
            $('#warningOnDelete').modal('show')
        }
    }),
    //
    // Fill in edit form when edit btn is clicked
    //
    $("#edit").click(function () {
        var data = $("#vulntable").bootstrapTable('getSelections');
        if(data.length > 1){
            $('#msgInfo').text("Please choose only one row for editing.");
            $('#infoModal').modal('show');
        }
        else if (data.length == 1) {
            $('#id_name_edit').val(data[0].name);
            $('#id_levelRisk_edit').val(data[0].levelRisk);
            $('#id_cve_edit').val(data[0].cve);
            $('#id_service_edit').val(data[0].service.id);
            $('#id_observation_edit').val(data[0].observation);
            $('#id_recommendation_edit').val(data[0].recommendation);
            $('#id_description_edit').val(data[0].description);
            $('#editVulnModal').modal('show');
            rowIDSelected = data[0].id;
        }
    }),

    $("#vulntable").change(function () {
        var data = $("#vulntable").bootstrapTable('getSelections');
        var editBtn = $("#edit");
        var delBtn = $("#delete");
        if(data.length!=1){
            editBtn.addClass("disabled");
        }
        else{
            editBtn.removeClass("disabled");
        }
        if(data.length==0 ){
            delBtn.addClass("disabled");
        }
        else{
            delBtn.removeClass("disabled");
        }
    })
);

// Format Href for bootstrap table
function HrefFormater(value, row, index) {
    return '<a href="' + row.id + '"> ' + row.name +'</a>';
}