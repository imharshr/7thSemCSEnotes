<!--
    7. Write a PHP program to display a digital clock which displays the current time of the
    server.
-->
<!DOCTYPE html>
<html>
 <head>
 <meta charset="UTF-8">
 <meta http-equiv="refresh" content="1">
 </head>
 <body>
 <h1>Display Current Date & Time</h1>
 <h2>
 <?php
 echo "The time from the server is <span style='color:blue';> " . date("h: i : s A")."</span>";
 echo '<br />';
 ?>
 </h2>
 </html>