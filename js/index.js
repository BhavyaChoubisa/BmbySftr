$(document).ready(function (){
   $('#example').DataTable({
      "pageLength": 5,
      "bLengthChange": false,
      ajax: "new_form/data.json",
      "columns": [
          { data: "first_name"}, 
          { data: "last_name"}, 
          { data: "email" }, 
          { data: "mobile"},
          { data: "age"},
          { data: "dob"},
          { data: "location"}
      ]
   });
});
