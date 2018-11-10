<?php 
#API access key from Google API's Console
    define( 'API_ACCESS_KEY', 'AAAA3ER_6vU:APA91bEYOCIJ1QpLjAjQVcGO2TsSvr6wajg_imaZbKQXNneu9ASx-1Br7O5wWZVMOdwIfWF6Fd4_SFI7UmarJuJhGTFUOVizSem16qfbOzpVqtMpU0to37Td63CfpjY24bKHRmQeuBzO');
    //$registrationIds = 'cN9JAA3mQ-Q:APA91bGigAF19cCDIxPjWQtOCTyVNYYgpiPNQTEJ_V9CSko9AXXOPWaH2LNwJWVoYKf5aAdvzC_n8RXiv6wAVKcd-ddF57SkDTj6arxpYU6YTx9iKnRM0J339O6nuSsmFf_aIoXHIK69';

    //$msg_title = "제목";
    //$msg_body = "내용";
    //push_msg("제목", "내용");
    function push_msg($msg_title, $msg_body){
        #prep the bundle
        $registrationIds = 'cN9JAA3mQ-Q:APA91bGigAF19cCDIxPjWQtOCTyVNYYgpiPNQTEJ_V9CSko9AXXOPWaH2LNwJWVoYKf5aAdvzC_n8RXiv6wAVKcd-ddF57SkDTj6arxpYU6YTx9iKnRM0J339O6nuSsmFf_aIoXHIK69';

        $msg = array
        (
            'body' 	=> $msg_body,
            'title'	=> $msg_title
        );
        $fields = array
            (
                'to'		=> $registrationIds,
                'notification'	=> $msg
            );
        $headers = array
            (
                'Authorization: key=' . API_ACCESS_KEY,
                'Content-Type: application/json'
            );
        #Send Reponse To FireBase Server	
        $ch = curl_init();
        curl_setopt( $ch,CURLOPT_URL, 'https://fcm.googleapis.com/fcm/send' );
        curl_setopt( $ch,CURLOPT_POST, true );
        curl_setopt( $ch,CURLOPT_HTTPHEADER, $headers );
        curl_setopt( $ch,CURLOPT_RETURNTRANSFER, true );
        curl_setopt( $ch,CURLOPT_SSL_VERIFYPEER, false );
        curl_setopt( $ch,CURLOPT_POSTFIELDS, json_encode( $fields ) );
        $result = curl_exec($ch );
        curl_close( $ch );
        #Echo Result Of FireBase Server
        echo $result;

    } 
?>