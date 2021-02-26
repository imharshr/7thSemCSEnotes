<!DOCTYPE html>
<html>
   <head>
      <meta charset="UTF-8">
      <title></title>
   </head>
   <body>
      <h1>Simple Calculator Using PHP</h1>
      <form method="post">
         <table>
            <tr>
               <td>Enter First Number: </td>
               <td><input type="text" name="first" required
                  autocomplete="off"/></td>
            </tr>
            <tr>
               <td>Enter Second Number: </td>
               <td><input type="text" name="second" required
                  autocomplete="off"/></td>
            </tr>
            <tr>
               <td>Select Operator: </td>
               <td>
                  <select name="op">
                     <option>Select Operation</option>
                     <option value="+">Addition</option>
                     <option value="-">Subtraction</option>
                     <option value="*">Multiplication</option>
                     <option value="/">Division</option>
                     <option value="%">Remainder</option>
                  </select>
               </td>
            </tr>
            <tr>
               <td colspan="2"><input type="submit" name="pop" value="Perform Operation"/></td>
            </tr>
         </table>
      </form>
    <?php
    if (isset($_POST['pop']))
    {
        echo "<h1>Result is </h1>";
        $num1 = $_POST["first"];
        $num2 = $_POST["second"];
        $op = $_POST["op"];
        $result = 0;
        switch ($op)
        {
            case '+':
                $result = $num1 + $num2;
                echo "<h1>Addition of 2 Numbers: " . $result . "</h1>";
            break;
            case '-':
                $result = $num1 - $num2;
                echo "<h1>Subtraction of 2 Numbers: " . $result . "</h1>";
            break;
            case '*':
                $result = $num1 * $num2;
                echo "<h1>Product of 2 Numbers: " . $result . "</h1>";
            break;
            case '/':
                $result = $num1 / $num2;
                echo "<h1>Division of 2 Numbers: " . $result . "</h1>";
            break;
            case '%':
                $result = $num1 % $num2;
                echo "<h1>Remainder of 2 Numbers: " . $result . "</h1>";
            break;
            default:
                echo "<h1 style='color:red;'>Sorry, No Operation Found</h1>";
            break;
        }
    }
    ?>
    </body>
</html>
