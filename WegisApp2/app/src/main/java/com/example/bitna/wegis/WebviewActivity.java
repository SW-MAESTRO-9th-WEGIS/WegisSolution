package com.example.bitna.wegis;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class WebviewActivity extends AppCompatActivity {

    private WebView WV;
    private WebSettings WS;
TextView tv;
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
        WV.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        WV.setWebChromeClient(new ChromeClient());

        WV.loadUrl("http://192.168.201.1/streamlog.php");




        Toast.makeText(WebviewActivity.this, "http://192.168.201.1/streamlog.php", Toast.LENGTH_LONG).show();
    }
    private class ChromeClient extends WebChromeClient{

    }
}

