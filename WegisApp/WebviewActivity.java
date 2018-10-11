package com.example.bitna.wegistest;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;

public class WebviewActivity extends AppCompatActivity {

    private WebView WV;
    private WebSettings WS;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_webview);


        Button tab1 = (Button) findViewById(R.id.tabBtn1);
        tab1.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(WebviewActivity.this,MainActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );


        Button tab2 = (Button) findViewById(R.id.tabBtn2);
        tab2.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(WebviewActivity.this,EventListActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );

        Button tab4 = (Button) findViewById(R.id.tabBtn4);
        tab4.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(WebviewActivity.this,ControlActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );
        WV = (WebView) findViewById(R.id.webV);
        WV.setWebViewClient(new WebViewClient());
        WS = WV.getSettings();
        WS.setJavaScriptEnabled(true);

        WS.setMediaPlaybackRequiresUserGesture(false);

// 뷰 가속 - 가속하지 않으면 영상실행 안됨, 소리만 나온다
        WV.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        WV.setWebChromeClient(new ChromeClient());
        WV.loadUrl("http://52.78.20.161/maestro/index.php?id=180707");


    }
    private class ChromeClient extends WebChromeClient{

    }
}

