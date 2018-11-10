#!/usr/local/bin/php -q 
<?php
//2가 나랑 빛나 언니
//echo "dddd";
//타임스템프가 같은게 몇번 있냐 >> 사람 수 판별 
//매치 페이스 찾기 >> 있으면 있고, 여뵤으면 페이스 갯수 세바
// person에 face 찾기 >>
// 두사람이 있는거 알았고 매치 페이스도 있다는 거 알았음 그 다음은? 인덱스로 봐야하나??

rekognition();


function rekognition(){
    //결과 파일 읽어 오기
    $arr = json_decode(file_get_contents('face_search_result.json'), true);

    $before_time = 0;
    $maxPeople = 0;
    $numPeople =1; //한 프레임 안의 사람 수 >> 사람 수로 생각 할래...
    $timestamp = array();

    foreach ($arr['Persons'] as $key => $value){
        $time = $value['Timestamp'];

        if($before_time == 0 || $before_time != $time){
            //값이 처음 들어오거나 이전시간과 다를 경우
            $maxPeople = 1;
            $addarr = array($maxPeople, $time);
            array_push($timestamp, $addarr);
            $before_time = $time;

        }else if($before_time == $time){
            //이전값이랑 값이 같다면
            $maxPeople++;
            $addarr = array($maxPeople, $time);
            array_push($timestamp, $addarr);
            $before_time = $time;
            
            if($maxPeople > $numPeople){
                $numPeople = $maxPeople;
            }
        }
        
    }

    $index = -1; //얼굴 빨리 찾기 위해
    $face_id = array();
    foreach ($timestamp as $key => $value){
        $num = $value[0];
        
        //print_r($timestamp);
        $index++;
        
        // 최대 값을 가진 애들 중에서 얼굴매칭 값 뽑아내자
        if($num == $numPeople){
            $index2 = $index;

            // 사람 수 만큼 타임스템프가 같은 인자들이 존재, 인덱스가 작음
            for($index2;$index2 > $index-$num; $index2--){
                $searchArr = $arr['Persons'][$index2];
                if(array_key_exists('FaceMatches', $searchArr) && $searchArr['FaceMatches']!=array()){
                    //얼굴 값
                    array_push($face_id , $searchArr['FaceMatches'][0]['Face']['FaceId']);

                }

            }
        }
    }
    //중복 제거
    $face_id = array_unique($face_id); //알고 있는 얼굴
    //데이터베이스 호출1

    $known = count($face_id);
    $unkown = $numPeople - $known;

    
    //중복 제거
    $face_id = array_unique($face_id); //알고 있는 얼굴
    //페이스 갯수만큼 얼굴데이터 넣기 & 얼굴이랑 비디오 매칭 테이블 넣기
    //$face_num = count($face_id);
    
 
    $conn = new mysqli("localhost", "wegis", "!pidb", "wegis");
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }


    foreach ($face_id as $key => $face){
        $sql = "insert into wegisFace (faceID, fileName) values('$face', '$face');";
        $conn->query($sql);
    }

    $conn->close();

    //shell_exec("ls > ok222222.json");
    //데이터베이스 호출2
    //여기서 디비에 얼굴 잘라 넣기

    //echo "전체: ".$numPeople."명 | 아는 사람: ".$known."명 | 모르는 사람: ".$unkown."\n";



    //$index =225;
    //print_r($arr['Persons'][$index]['FaceMatches'][0]['Face']['FaceId']);
    //print_r($timestamp);
    //print_r($arr['Persons'][225]);
    //print_r($arr['Persons'][226]);
    /*
    if(array_key_exists('FaceMatches', $arr['Persons'][225])){

        echo "ok";
    }
    */

    //echo $index;
}

?>