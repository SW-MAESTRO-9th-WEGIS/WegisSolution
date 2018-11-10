<?php

    $link=mysqli_connect("localhost", "wegis", "!pidb", "wegis");
    if (!$link)
    {
        echo "MySQL 접속 에러 : ";
        echo mysqli_connect_error();
        exit();
    }

    mysqli_set_charset($link,"utf8");


    $sql="select * from wegisVideo";

    $result=mysqli_query($link,$sql);
    $data = array();
    if($result){

        while($row=mysqli_fetch_array($result)){
            array_push($data,
                array('ID'=>$row[0],
                'fileName '=>$row[1],
                'DATE'=>$row[2],
                'TIME'=>$row[3],
                'duringTime'=>$row[4],
                'numPerson'=>$row[5],
                'Keypad'=>$row[6],
                'safetyLevel'=>$row[7]
            ));
        }
        header('Content-Type: application/json; charset=utf8');
        $json = json_encode(array("webnautes"=>$data), JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
        echo $json;

    }
    else{
        echo "SQL문 처리중 에러 발생 : ";
        echo mysqli_error($link);
    }

    mysqli_close($link);

?>