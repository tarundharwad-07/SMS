<?php
include 'db.php';
$id = $_GET['id'];
$sql = "DELETE FROM STUDENT WHERE STU_ID = $id";
echo json_encode(["status" => $conn->query($sql) ? "deleted" : "error"]);
?>