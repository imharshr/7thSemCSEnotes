<?php

$allTheStates = "Mississippi Alabama Texas Massachusetts Kansas";

echo "<h3>Given sentence is $allTheStates </h3>";

$statesArray = [];
$states1 = explode(' ', $allTheStates);
$i = 0;

foreach ($states1 as $state) {
 if (preg_match('/xas$/', ($state))) {
 $statesArray[$i] = ($state);
 $i = $i + 1;
 echo "\nThe States that ends in xas: " . $state;
 }
}

foreach ($states1 as $state) {
 if (preg_match('/^k.*s$/i', ($state))) {
 $statesArray[$i] = ($state);
 $i = $i + 1;
 echo "<br>\nThe states that begins with k ans ends in s (case-sensitive) : " . $state;
 }
}

foreach($states1 as $state) {
if (preg_match('/^M.*s$/', ($state))) {
 $statesArray[$i] = ($state);
 $i = $i + 1;
 echo "<br>\nThe states that begins with M and ends in s: " . $state;
}
}

foreach($states1 as $state) {
if (preg_match('/a$/', ($state))) {
 $statesArray[$i] = ($state);
 $i = $i + 1;
 echo "<br>\nThe states that ends in a: " . $state . "<br>";
}
}
foreach ($statesArray as $element => $value) {
 print( "<br>\n element[" . $element . "] = " . $value );
}
?>
