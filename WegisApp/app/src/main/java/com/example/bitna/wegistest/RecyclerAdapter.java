package com.example.bitna.wegistest;

import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;


public class RecyclerAdapter extends RecyclerView.Adapter<RecyclerAdapter.ViewHolder> {

    private ArrayList<EventListActivity.item> mDataset; //MainActivity에 item class를 정의해 놓았음

    // Provide a reference to the views for each data item
    // Complex data items may need more than one view per item, and
    // you provide access to all the views for a data item in a view holder
    public static class ViewHolder extends RecyclerView.ViewHolder {
        // 사용될 항목들 선언
        public TextView mTime;
        public TextView mFeature;

        public ImageView mPhoto;

        public ViewHolder(View v) {
            super(v);

             mTime = (TextView) v.findViewById(R.id.time);
             mFeature = (TextView) v.findViewById(R.id.feature);

        }
    }

    // 생성자 - 넘어 오는 데이터파입에 유의해야 한다.
    public RecyclerAdapter(ArrayList<EventListActivity.item> myDataset) {
        mDataset = myDataset;

    }

    //뷰홀더
    // Create new views (invoked by the layout manager)
    @Override
    public RecyclerAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        // create a new view
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_card, parent, false);
        // set the view's size, margins, paddings and layout parameters

        ViewHolder holder = new ViewHolder(v);
        return holder;
    }

    // Replace the contents of a view (invoked by the layout manager)
    @Override
    public void onBindViewHolder(ViewHolder holder, int position) {
        // - get element from your dataset at this position
        // - replace the contents of the view with that element

        holder.mTime.setText(mDataset.get(position).getTime());
        //holder.mTime.setText(Integer.toString(mDataset.size()));
        holder.mFeature.setText(String.valueOf(mDataset.get(position).getFeature()));
        //holder.mPhoto.setImageBitmap(mDataset.get(position).getPhoto()); //첨부된 이미지를 연결해줘야 하는데 이건 또 복잡하다. 이건 나중에...
    }

    @Override
    public int getItemCount() {
        return mDataset.size();
    }
}
