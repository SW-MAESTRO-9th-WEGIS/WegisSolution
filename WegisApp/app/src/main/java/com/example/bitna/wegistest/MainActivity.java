package com.example.bitna.wegistest;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {


    static final String[] LIST_MENU = {"LIST1", "LIST2", "LIST3"} ;
    TextView tv1,tv2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv1 = (TextView) findViewById(R.id.privaTV) ;
        tv2 = (TextView)  findViewById(R.id.saferTV);

        Button tab3 = (Button) findViewById(R.id.tabBtn3);
        tab3.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(MainActivity.this,WebviewActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );

        Button tab2 = (Button) findViewById(R.id.tabBtn2);
        tab2.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(MainActivity.this,EventListActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );


        ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1, LIST_MENU) ;

        ListView listview = (ListView) findViewById(R.id.listV1) ;
        listview.setAdapter(adapter) ;


        Button tab4 = (Button) findViewById(R.id.tabBtn4);
        tab4.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(MainActivity.this,ControlActivity.class);
                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );

    }
}
