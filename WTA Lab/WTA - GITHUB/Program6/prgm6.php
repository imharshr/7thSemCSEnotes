<!--
    6. Write a PHP program to keep track of the number of visitors visiting the web page
    and to display this count of visitors, with proper headings.
-->
<?php
$file = 'counter.txt';
$count = strval(file_get_contents($file));
file_put_contents($file, $count + 1); 
echo("<h1>You are visitor number: ".$count."</h1>"); 
?>
