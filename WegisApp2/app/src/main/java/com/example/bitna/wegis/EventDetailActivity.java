package com.example.bitna.wegis;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class EventDetailActivity extends AppCompatActivity {
TextView tvTime,tvDe,tvDe2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_event_detail);
    tvTime= (TextView) findViewById(R.id.tvTime);
    tvDe = (TextView) findViewById(R.id.tvDesc);
        tvDe2 = (TextView) findViewById(R.id.tvDesc2);
    tvTime.setText(" 9/30 13:00\n"+" 머문 시간 47 초");
    tvDe.setText("도어락 접촉 시도");
    tvDe2.setText("감지된 사람 1 명");



    }
}
