#!/bin/bash

# 비디오 변수를 매게변수로 받아오기
# 환경 변수로 선언해야 다른 스크립트에서 사용이 가능
export video_name=$1
echo ${video_name} > name.json
# export video_name="test01.mp4"

# 비디오 업로드
aws s3 cp /home/pi/Videos/${video_name} s3://wegis-rekognition-video
#aws s3 cp /home/pi/Videos/2018-11-02_16:38:02.mp4 s3://wegis-rekognition-video

# 얼굴검색
aws rekognition start-face-search --collection-id "wegisface" --video '{"S3Object":{"Bucket":"wegis-rekognition-video","Name":"'${video_name}'"}}' > face_search_id.json
#aws rekognition start-face-search --collection-id "wegisface" --video '{"S3Object":{"Bucket":"wegis-rekognition-video","Name":"2018-11-02_16:38:02.mp4"}}' > face_search_id.json

# face_search.json의 JobId받아오기 ``````
JobId=`cat face_search_id.json | jq '.JobId' | tr -d '"'`
# echo ${JobId}

# start-face-search 결과값 호출 및 저장
aws rekognition get-face-search --job-id ${JobId} > face_search_result.json
#JobStatus확인
JobStatus=`cat face_search_result.json | jq '.JobStatus' | tr -d '"'`

# 상태값 확인
while [ ${JobStatus} != "SUCCEEDED" ]
do
        aws rekognition get-face-search --job-id ${JobId} > face_search_result.json
        JobStatus=`cat face_search_result.json | jq '.JobStatus' | tr -d '"'`
done

# 반환값에 따라 추가 동작 지정
# 결과 값 파싱 및 동작을 지원하는 php 호출

php parse_result.php
#php face_insert.php

# echo ${JobStatus}