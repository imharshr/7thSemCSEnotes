<?php
$states=$_POST['t1'];
echo "<h3>Given sentence is $states </h3><br>";
$list=array();
$keywords=preg_split("/\s+/",$states);
foreach ($keywords as $word)
{
if(preg_match('/xas$/', $word))
{
echo "Word $word ends in xas : ".$word."<br>";
$list[0]=$word;
}
}
foreach ($keywords as $word)
{
if(preg_match('/^k.*s$/i', $word))
{
echo "Word $word begins with k and ends s: ".$word."<br>";
$list[1]=$word;
}
}
foreach ($keywords as $word)
{
if(preg_match('/^M.*s$/', $word))
{
echo "Word $word begins with M and ends s: ".$word."<br>";
$list[2]=$word;
}
}
foreach ($keywords as $word)
{
if(preg_match('/a$/', $word))
{
echo "Word $word ends with a : ".$word."<br>";
$list[3]=$word;
}
}
//echo "<h3>List contents: ". implode(', ',$list );
?>
