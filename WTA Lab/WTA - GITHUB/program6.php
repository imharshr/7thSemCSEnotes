<!--
    6. Write a PHP program to keep track of the number of visitors visiting the web page
    and to display this count of visitors, with proper headings.
-->
<?php
$fp = fopen("counter.txt", "r");
$count = fread($fp,1024);
fclose($fp);
$count = $count + 1;
echo "<p> Page Views: " . $count . "<p>";
$fp = fopen("counter.txt", "w");
fwrite($fp,$count);
fclose($fp);
?>
