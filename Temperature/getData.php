<?php
// Подключение к базе данных

// Параметры подключения к базе данных
$servername = "localhost";
$username = "serg153e_temp";
$password = "123Qwe";
$dbname = "serg153e_temp";

// Создание подключения
$conn = new mysqli($servername, $username, $password, $dbname);

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
    if ($row['Stat'] == 1) {
        echo "<b>Вкл</b>";
         
    } else {
        echo '<b>Выкл</b>';
        
    }

echo '</div>';

?>
