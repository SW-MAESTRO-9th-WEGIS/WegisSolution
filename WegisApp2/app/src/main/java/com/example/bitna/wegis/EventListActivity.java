package com.example.bitna.wegis;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

public class EventListActivity extends AppCompatActivity {

    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;

    // 아이템 리스트
    //   private String[] myDataset;


    private static ArrayList<item> itemArrayList;
    Button tab1,tab3,tab4;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_event_list);

    Bundle b = getIntent().getExtras();
    ArrayList<String> date = b.getStringArrayList("date");
    ArrayList<String> time = b.getStringArrayList("time");
    ArrayList<String> due = b.getStringArrayList("due");
    ArrayList<Integer> numPerson = b.getIntegerArrayList("numPerson");

        ArrayList<Integer> keypad = b.getIntegerArrayList("keypad");

        Button tab1 = (Button) findViewById(R.id.tabBtn1);
        tab1.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(EventListActivity.this,MainActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );


        Button tab3 = (Button) findViewById(R.id.tabBtn3);
        tab3.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(EventListActivity.this,WebviewActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );

        Button tab4 = (Button) findViewById(R.id.tabBtn4);
        tab4.setOnClickListener( new Button.OnClickListener() {
                                     public void onClick(View v) {
                                         Intent intent =  new Intent(EventListActivity.this,ControlActivity.class);

                                         startActivity(intent);
                                         overridePendingTransition(0,0);
                                     }
                                 }
        );
        //데이터준비-실제로는 ArrayList<>등을 사용해야 할듯 하다.
        //인터넷이나 폰에 있는 DB에서 아이템을 가져와 배열에 담아 주면 된다.
        //myDataset = new String[]{"도봉순", "이순신", "강감찬","세종대왕"};
        //ArrayList 생성



        itemArrayList = new ArrayList<>();
        for(int i=0;i<date.size();i++){


        itemArrayList.add(new item(date.get(i).toString(),time.get(i).toString(),due.get(i).toString(), keypad.get(i),numPerson.get(i),null));}


        mRecyclerView = (RecyclerView) findViewById(R.id.recyclerview);
//        mRecyclerView.setHasFixedSize(true);//옵션
        //Linear layout manager 사용
        mLayoutManager = new LinearLayoutManager(this);
        mRecyclerView.setLayoutManager(mLayoutManager);

        //어답터 세팅
        mAdapter = new RecyclerAdapter(itemArrayList); //스트링 배열 데이터 인자로
        mRecyclerView.setAdapter(mAdapter);
    }


    //아이템 클라스
    public class item {
        String date;
        String time;
        String due;
        String photo;
        int numPerson;
        int keypad;

        public item(String date, String time,  String due, int numPerson, int keypad,String photo) {
            this.date = date;
            this.time = time;
            this.due =  due;
            this.numPerson = numPerson;
            this.keypad = keypad;
          //  this.photo = photo;
        }
        public String getDate(){return date;}
        public String getTime() {
            return time;
        }
        public String getDue() {
            return due;
        }
        public int getNumperson(){return numPerson;}
        public int getKeypad(){return keypad;}
        public String getPhoto() {
            return photo;
        }
    }
}


