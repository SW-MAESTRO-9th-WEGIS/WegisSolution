#!/usr/local/bin/php -q 
<?php
//include "./db_conn.php";  
//include "./send_fcm.php";  
$result = json_decode(file_get_contents('php://input'), true);
/* checking input data option : argv[1]
0 : IP
1 : emergency data 
2 : video meta data
*/

switch ($result[check]) {
    case 0:
        // 환경변수 설정 >> 스크립트로 넣기
        exec("export DOORLOCK_IP=".$result['ip']);
        break;
    case 1:
        $duringTime = $result['duringtime'];
        $Keypad = $result['keypad'];
        $str_msg = "머문 시간: ".$duringTime." / 키패드 누름 횟수: ".$Keypad;
        // 알림 스크립트
        push_msg("위험이 감지되었습니다.", $str_msg);
        break;
    case 2:
        // DB에 데이터 넣기, substr(문자열, 시작위치, 길이)
        $fileName = $result[file_name];
        $DATE = substr($result[file_name],9);
        $TIME = substr($result[file_name],0,9);
        $duringTime = $result[duringTime];
        $Keypad = $result[Keypad];

        $conn = new mysqli("localhost", "wegis", "!pidb", "wegis");
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }
        
        $sql = "insert into wegisVideo (fileName, DATE, TIME, duringTime, Keypad) ";
        $sql .= "values('$fileName', '$DATE', '$TIME', '$duringTime', '$Keypad') ;";    
        $conn->query($sql);
        $conn->close();
        //push_msg("영상받기 완료", $fileName);
        // aws 영상 넣기 >> 여기 안에서 영상처리 실행함수 호출 함.

        $fileName = "2018-11-02_16:38:02";
        shell_exec("./rekognition.sh {$fileName}.mp4");

        include "./send_fcm.php";  
        push_msg("영상처리도 완료!", "확인 고고");
        break;
}

?>
