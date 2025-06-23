<?php
include 'db.php';
$name = $_GET['name'];
$sql = "SELECT * FROM STUDENT WHERE STU_NAME LIKE '%$name%'";
$result = $conn->query($sql);
$data = [];
while($row = $result->fetch_assoc()) { $data[] = $row; }
echo json_encode($data);
?>