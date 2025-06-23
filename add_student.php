<?php
include 'db.php';
$data = json_decode(file_get_contents("php://input"), true);
$name = $data['name'];
$fee = $data['fee'];
$result = $data['result'];
$usn = $data['usn'];
$branch = $data['branch'];
$sql = "INSERT INTO STUDENT (STU_NAME, STU_Fee_details, STU_Exam_result, STU_USN, STU_BRANCH)
        VALUES ('$name', '$fee', '$result', '$usn', '$branch')";
echo json_encode(["status" => $conn->query($sql) ? "success" : "error"]);
?>