<?php
if(!isset($_POST['submit'])){
    echo "error; you need to submit the form!";
}

$name = $_POST['name'];
$visitor_email = $_POST['email'];
$message = $_POST['message'];

if(empty($name) || empty($visitor_email)){
    echo "Name and email are mandatory!";
    exit;
}

$email_from = 'geetsalame156@gmail.com';
$email_subject = "PhoneFits Feedback";
$email_body = "Feedack : \n Name : $name \n Feedback : $message \n";
$email_to = "geetsalame156@gmail.com";
$headers = "From : $email_from \r\n";

mail($email_to, $email_subject, $email_body, $headers);
?>