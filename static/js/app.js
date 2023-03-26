$(document).ready(function() {
    console.log('page load');
  
    // Make an API call to list incidents
    $.ajax({
      url: "list_incidents",
      type: "GET",
      dataType: "json",
      success: function(response) {
  
          console.log(response)
        // Populate the table with the incidents data
        var incidents = response.incidents;
        var $tableBody = $('#incident-table').find('tbody');
        $.each(incidents, function(index, incident) {
          var $row = $('<tr>');
          $row.append($('<td>').text(incident.incident_id));
          $row.append($('<td>').text(incident.reporter));
          $row.append($('<td>').text(incident.incident_details));
          $row.append($('<td>').text(incident.reported_date));
          $row.append($('<td>').text(incident.priority));
          $row.append($('<td>').text(incident.status));
          if (incident.status == 'Open' || incident.status == 'In Progress') {
            $row.append($('<td>').html('<a href="/update_incident?incident_id=' + incident.incident_id + '&reporter=' + incident.reporter + '" class="btn btn-primary">Edit</a>'));
          } else {
            $row.append($('<td>'));
          }
          $tableBody.append($row);
        });
      },
      error: function(response) {
        console.log("Error occurred while fetching incidents.");
      }
    });
  });
  