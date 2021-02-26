<?php
header('Content-Type: text/plain');

$matrix1 = array(
    array(
        1,
        2
    ) ,
    array(
        4,
        5
    )
);
$matrix2 = array(
    array(
        4,
        6
    ) ,
    array(
        1,
        8
    )
);
echo "\n\n\n";
echo "The order of the matrix A is: " . count($matrix1) . "x" . count($matrix1[0]);
echo "\n";
echo "The order of the matrix B is: " . count($matrix2) . "x" . count($matrix2[0]);
echo "\n";

$rowCount = count($matrix1);
$colCount = count($matrix1[0]);
$rowCount2 = count($matrix2);
$colCount2 = count($matrix2[0]);

echo "\n The input matrix A is:\n";
for ($r = 0;$r < $rowCount;$r++)
{
    for ($c = 0;$c < $colCount;$c++)
    {
        echo $matrix1[$r][$c] . " \t";
    }
    echo "\n";
}

echo "\n The input matrix B is:\n";
for ($r = 0;$r < $rowCount;$r++)
{
    for ($c = 0;$c < $colCount;$c++)
    {
        echo $matrix2[$r][$c] . " \t";
    }
    echo "\n";
}

echo "\nTranspose of matrix 1 is:\n";
for ($r = 0;$r < $colCount;$r++)
{
    for ($c = 0;$c < $rowCount;$c++)
    {
        echo $matrix1[$c][$r] . " \t";
    }
    echo "\n";
}

echo "\nTranspose of matrix 2 is:\n";
for ($r = 0;$r < $colCount2;$r++)
{
    for ($c = 0;$c < $rowCount2;$c++)
    {
        echo $matrix2[$c][$r] . " \t";
    }
    echo "\n";
}

echo "\nThe sum of matrix is:\n";
for ($r = 0;$r < $rowCount;$r++)
{
    for ($c = 0;$c < $colCount;$c++)
    {
        $val = $matrix1[$r][$c] + $matrix2[$r][$c];
        echo $val . "\t";
    }
    echo "\n";
}

echo "\nThe Multiplication of matrix is:\n";
if ($colCount == $rowCount2)
{

    $result = array();
    for ($i = 0;$i < $rowCount;$i++)
    {
        for ($j = 0;$j < $colCount2;$j++)
        {
            $result[$i][$j] = 0;
            for ($k = 0;$k < $rowCount2;$k++)
            {
                $result[$i][$j] += $matrix1[$i][$k] * $matrix2[$k][$j];
            }
            echo $result[$i][$j] . " \t";
        }
        echo "\n";

    }
}
else
{
    echo "The matrix multiplication is not possible.";
}
?>
