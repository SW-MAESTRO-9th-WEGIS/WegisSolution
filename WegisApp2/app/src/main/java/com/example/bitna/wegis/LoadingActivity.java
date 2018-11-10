package com.example.bitna.wegis;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class LoadingActivity extends Activity {
    String userID;
    private static String TAG = "Getting_Scorelist";

    private static String TAG_TIME1 = "time";
    private static String TAG_TIME2 = "time";
    private static String TAG_DESC = "title";
    private static String TAG_LEVEL = "title";

    private static String TAG_KEY = "key";
    private static final String TAG_JSON="data";
    String mJsonString;

    ArrayList<String> arrlevel;
    ArrayList<String> arrStime;
    ArrayList<String> arrTtime;
    ArrayList<String> arrDesc;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_loading);

            startActivity(new Intent(LoadingActivity.this, MainActivity.class));
        }

    }
