<?php
$host = "localhost";
$user = "root";
$pass = "Tarun@123";
$dbname = "studentmanagementsys";

$conn = new mysqli($host, $user, $pass, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>