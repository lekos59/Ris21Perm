<?php
// Подключение к базе данных

// Параметры подключения к базе данных
$servername = "localhost";
$username = "serg153e_temp";
$password = "123Qwe";
$dbname = "serg153e_temp";

// Создание подключения
$conn = new mysqli($servername, $username, $password, $dbname);
////////////////////////////////////
if(isset($_POST['action']) && $_POST['action'] == 'OFF') 
    {
        $query = "UPDATE `Status` SET `Status`= 0 WHERE ID = 1";
        $result = mysqli_query($conn, $query); 
    }

else if (isset($_POST['action']) && $_POST['action'] == 'ON')
     {
        $query = "UPDATE `Status` SET `Status`= 1 WHERE ID = 1";
        $result = mysqli_query($conn, $query); 
    }
else if (isset($_POST['action']) && $_POST['action'] == 'AUTO')
     {
        $query = "UPDATE `Status` SET `Status`= 2 WHERE ID = 1";
        $result = mysqli_query($conn, $query); 
    }

/////////////////////////////

// Проверка соединения
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Запрос данных из таблицы
$sql = "SELECT Id, Temp, Stat FROM `Temperature` ORDER BY Id DESC LIMIT 1"; 

 $result = $conn->query($sql); 

// Вывод данных
echo '<div style="text-align:center; color:red; font-size:55px;">';
foreach ($result as $row) {
    echo '<b>'. $row['Temp']. '</b><br>'. '<br>';
}
    if ($row['Stat'] == 0) {
        echo "<b>Выкл</b>";
         
    } else if ($row['Stat'] == 1) {
        echo '<b>Вкл</b>';
        
    }   else if ($row['Stat'] == 2) {
        echo "<b>Авто Вкл</b>";
         
    } else if ($row['Stat'] == 3) {
        echo '<b>Авто Выкл</b>';
        
    }

echo '</div>';

?>
