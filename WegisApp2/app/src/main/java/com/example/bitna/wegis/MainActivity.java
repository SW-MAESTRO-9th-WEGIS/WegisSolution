package com.example.bitna.wegis;


import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.util.Log;
import android.view.View;

import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {


    static final String[] LIST_MENU = {"LIST1", "LIST2", "LIST3"};
    TextView tv1, tv2;
    View view;
    ListView lv;
    private static String TAG = "MainActivity";

    private static String TAG_DATE = "DATE";
    private static String TAG_TIME = "TIME";
    private static String TAG_DUE = "duringTime";
    private static String TAG_LEVEL = "safetyLevel";
    private static String TAG_NUMPER = "numPerson";
    private static String TAG_KEYPAD = "Keypad";
    private static String TAG_KEY = "key";
    private static final String TAG_JSON="webnautes";
    String mJsonString;


    ArrayList<String> arrDate;
    ArrayList<String> arrTime;
    ArrayList<String> arrDue;
    ArrayList<String> arrLevel;

    ArrayList<String> arrayList;
    ArrayList<Integer> arrNumP;
    ArrayList<Integer> arrKeypad;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        tv1 = (TextView) findViewById(R.id.privaTV);
        tv2 = (TextView) findViewById(R.id.saferTV);
        view = (View) findViewById(R.id.lv);

        Button safebtn = (Button) findViewById(R.id.safebtn);
        Button guardbtn = (Button) findViewById(R.id.guardbtn);


    arrDate = new ArrayList<>();
    arrTime = new ArrayList<>();
    arrDue = new ArrayList<>();
    arrLevel = new ArrayList<>();
    arrayList = new ArrayList<>();
    arrNumP = new ArrayList<>();
    arrKeypad = new ArrayList<>();

       GetData task = new GetData();
       task.execute("http://192.168.201.1/connection/getvideo.php");


        guardbtn.setOnClickListener(new Button.OnClickListener() {
                                        public void onClick(View v) {
                                            // view.animate().translationY(500).withLayer();
                                            // 다이얼로그 바디

                                            AlertDialog.Builder alertdialog = new AlertDialog.Builder(MainActivity.this);
                                            // 다이얼로그 메세지

                                            alertdialog.setMessage("집까지 안전하게 지켜봐드릴까요? \n" +
                                                    "집 도착 예상 시간은 '12분'");

                                            // 확인버튼
                                            alertdialog.setPositiveButton("확인", new DialogInterface.OnClickListener() {
                                                @Override
                                                public void onClick(DialogInterface dialog, int which) {
                                                    Toast.makeText(MainActivity.this, "집까지 가는 길 지켜봐줄께요~", Toast.LENGTH_LONG).show();
                                                    tv1.setText("안심 귀가 지키미\n 동작중");

                                                }
                                            });

                                            // 취소버튼
                                            alertdialog.setNegativeButton("취소 ( 5 )", new DialogInterface.OnClickListener() {

                                                @Override
                                                public void onClick(DialogInterface dialog, int which) {
                                                    Toast.makeText(MainActivity.this, "'취소'버튼을 눌렀습니다.", Toast.LENGTH_SHORT).show();
                                                }
                                            });
                                            // 메인 다이얼로그 생성
                                            AlertDialog alert = alertdialog.create();
                                            // 아이콘 설정
                                            alert.setIcon(R.drawable.pic_security_level);
                                            // 타이틀
                                            alert.setTitle("안심귀가 지킴이");
                                            // 다이얼로그 보기
                                            alert.show();

                                        }
                                    }
        );

        safebtn.setOnClickListener(new Button.OnClickListener() {
                                       public void onClick(View v) {
                                           // view.animate().translationY(500).withLayer();
                                           // 다이얼로그 바디
                                           AlertDialog.Builder alertdialog = new AlertDialog.Builder(MainActivity.this);
                                           // 다이얼로그 메세지
                                           alertdialog.setMessage("프라이버시 모드를 실행할까요?");

                                           // 확인버튼
                                           alertdialog.setPositiveButton("확인", new DialogInterface.OnClickListener() {
                                               @Override
                                               public void onClick(DialogInterface dialog, int which) {
                                                   Toast.makeText(MainActivity.this, "무효화 작동이 시작됩니다", Toast.LENGTH_LONG).show();
                                                   tv1.setText("프라이버시 모드 ON");

                                               }
                                           });

                                           // 취소버튼
                                           alertdialog.setNegativeButton("취소", new DialogInterface.OnClickListener() {

                                               @Override
                                               public void onClick(DialogInterface dialog, int which) {
                                                   Toast.makeText(MainActivity.this, "'취소'버튼을 눌렀습니다.", Toast.LENGTH_SHORT).show();
                                               }
                                           });
                                           // 메인 다이얼로그 생성
                                           AlertDialog alert = alertdialog.create();
                                           // 아이콘 설정
                                           alert.setIcon(R.drawable.pic_security_level);
                                           // 타이틀
                                           alert.setTitle("제목");
                                           // 다이얼로그 보기
                                           alert.show();

                                       }
                                   }
        );


        Button tab3 = (Button) findViewById(R.id.tabBtn3);
        tab3.setOnClickListener(new Button.OnClickListener() {
                                    public void onClick(View v) {
                                        Intent intent = new Intent(MainActivity.this, WebviewActivity.class);

                                        startActivity(intent);
                                        overridePendingTransition(0, 0);
                                    }
                                }
        );

        Button tab2 = (Button) findViewById(R.id.tabBtn2);
        tab2.setOnClickListener(new Button.OnClickListener() {
                                    public void onClick(View v) {

                                        Intent intent = new Intent(MainActivity.this,EventListActivity.class);
                                        intent.putStringArrayListExtra("date",arrDate);
                                        intent.putStringArrayListExtra("time",arrTime);
                                        intent.putStringArrayListExtra("due",arrDue);
                                        intent.putStringArrayListExtra("level",arrLevel);
                                        intent.putIntegerArrayListExtra("numPerson",arrNumP);
                                        intent.putIntegerArrayListExtra("keypad",arrKeypad);
                                        startActivity(intent);
                                        overridePendingTransition(0, 0);
                                    }
                                }
        );


        Button tab4 = (Button) findViewById(R.id.tabBtn4);
        tab4.setOnClickListener(new Button.OnClickListener() {
                                    public void onClick(View v) {
                                        Intent intent = new Intent(MainActivity.this, ControlActivity.class);
                                        startActivity(intent);
                                        overridePendingTransition(0, 0);
                                    }
                                }
        );
    }

    public class GetData extends AsyncTask<String, Void, String> {
        ProgressDialog progressDialog;
        String errorString = null;

        @Override
        protected void onPreExecute() {
            super.onPreExecute();

            progressDialog = ProgressDialog.show(MainActivity.this,
                    "Please Wait", null, true, true);
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            progressDialog.dismiss();
            //mTextViewResult.setText(result);
            Log.d(TAG, "response  - " + result);

            if (result == null){

                //mTextViewResult.setText(errorString);
            }
            else {
                mJsonString = result;
                showResult();
            }
        }

        @Override
        protected String doInBackground(String... params) {

            String serverURL = params[0];

           // String postParameters = "userID="+userID;
         //   Log.i("doinBack parameter",postParameters);
            try {

                URL url = new URL(serverURL);
                HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
                httpURLConnection.setRequestMethod("POST");
                httpURLConnection.setReadTimeout(5000);
                httpURLConnection.setConnectTimeout(5000);
                httpURLConnection.connect();

              /*  OutputStream outputStream = httpURLConnection.getOutputStream();
                outputStream.write(postParameters.getBytes("UTF-8"));
                outputStream.flush();
                outputStream.close();*/

                int responseStatusCode = httpURLConnection.getResponseCode();
                Log.d(TAG, "response code - " + responseStatusCode);

                InputStream inputStream;
                if (responseStatusCode == HttpURLConnection.HTTP_OK) {
                    inputStream = httpURLConnection.getInputStream();
                } else {
                    inputStream = httpURLConnection.getErrorStream();
                }


                InputStreamReader inputStreamReader = new InputStreamReader(inputStream, "UTF-8");
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

                StringBuilder sb = new StringBuilder();
                String line;

                while ((line = bufferedReader.readLine()) != null) {
                    sb.append(line);
                }

                bufferedReader.close();

                return sb.toString().trim();

            } catch (Exception e) {

                Log.d(TAG, "InsertData: Error ", e);
                errorString = e.toString();

                return null;
            }
        }
    }


    private ArrayList showResult(){
        try {

            Log.i("MainActivity","start show");
            JSONObject jsonObject = new JSONObject(mJsonString);
            JSONArray jsonArray = jsonObject.getJSONArray(TAG_JSON);
            Log.i("Json",jsonObject.toString());

            for(int i=0;i<jsonArray.length();i++){
                JSONObject item = jsonArray.getJSONObject(i);
                String date = item.getString(TAG_DATE);
                String time = item.getString(TAG_TIME);
                String due = item.getString(TAG_DUE);
                String level = item.getString(TAG_LEVEL);
                String numPerson = item.getString(TAG_NUMPER);
                String keypad = item.getString(TAG_KEYPAD);

                Log.d("Json",date);
                Log.d("Json",time);
                arrDate.add(i,date);
                arrTime.add(i,time);
                arrDue.add(i,due);
                arrLevel.add(i,level);
                arrNumP.add(i,Integer.parseInt(numPerson));
                arrKeypad.add(i,Integer.parseInt(keypad));
               // Log.i("MainActivity",arrkey.get(i));


            }
        } catch (JSONException e) {
            Log.d(TAG, "showResult : ", e);
        }

       arrayList.add("최근 방문 기록");

        for(int i=0;i<arrDate.size();i++){

            if(arrKeypad.get(i)>=1)
                arrayList.add(arrTime.get(i)+"  |  "+arrDate.get(i)+"  |  도어락 언락 시도감지");
            else if(arrNumP.get(i)>=2)arrayList.add(arrTime.get(i)+"  |  "+arrDate.get(i)+"  |  2명이상 방문감지");
            else arrayList.add(arrTime.get(i)+"  |  "+arrDate.get(i));
            Log.i("arrayList",arrayList.get(i));
            Log.i("arrayList",arrayList.get(i));
            Log.i("arrayList",arrayList.get(i));
        }
        ListView listview = (ListView) findViewById(R.id.listV1);
        ArrayAdapter adapter = new ArrayAdapter(this, R.layout.listview_item, arrayList);
        listview.setAdapter(adapter);
        return arrDate;
    }


}





