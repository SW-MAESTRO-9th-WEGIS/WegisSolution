<?php
$url = "http://192.168.201.1/connection/getdata.php";
//$url = "http://192.168.201.1/connection/eect.php";
$file_path = "./";
/* checking input data option : argv[1]
0 : IP
1 : emergency data 
2 : video meta data
*/

$check = $argv[1]; 
switch ($check) {
    case 0:
        $data = array(
            'check' => $argv[1],
            'ip' => $argv[2]
        );
        break;
    case 1:
        $data = array(
            'check' => $argv[1],
            'TIME' => $argv[2],
            'keypad' => $argv[3],
        ); 
        break;
    case 2:
        // 파일 업로드
        ftp_upload($file_path,$argv[2]); 
         
        // 비디오 데이터 전달    
        $data = array(
            'check' => $argv[1],
            'file_name' => $argv[2],
            'date_time' => $argv[3],
            'duringTime' => $argv[4]
           );
        break;
}

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_HEADER, FALSE);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json')); 
curl_setopt($ch, CURLOPT_POST, TRUE);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data)); 
$result = curl_exec($ch);
curl_close($ch);


function ftp_upload($file_path,$file_name){
    $ftp_host = "http://192.168.201.1/";
    $ftp_id = "pi";    
    $ftp_pw = "raspberry";  
    $ftp_port = "21";           
    $server_path = "/home/pi/Videos/"; 

    if(!($fc = ftp_connect($ftp_host, $ftp_port))) die("$ftp_host : $ftp_port - 연결에 실패");   
    if(!ftp_login($fc, $ftp_id, $ftp_pw)) die("$ftp_id - 로그인에 실패하였습니다.");   
    ftp_chdir($fc, $server_path);   
    $source_file = $file_path ."/" . $file_name;
    $destination_file = $file_name;
    if(!ftp_put($fc, $destination_file, $source_file, FTP_BINARY)) exit("디렉토리 이동 ");       
    echo "성공";
    ftp_quit($fc); 
}

?>
