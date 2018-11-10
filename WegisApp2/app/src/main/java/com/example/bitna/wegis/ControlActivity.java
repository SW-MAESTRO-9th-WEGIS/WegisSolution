package com.example.bitna.wegis;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class ControlActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_control);

        Button tab1 = (Button) findViewById(R.id.tabBtn1);
        tab1.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(ControlActivity.this,MainActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );


        Button tab2 = (Button) findViewById(R.id.tabBtn2);
        tab2.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(ControlActivity.this,EventListActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );

        Button tab3 = (Button) findViewById(R.id.tabBtn3);
        tab3.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(ControlActivity.this,ControlActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );
    }
}
