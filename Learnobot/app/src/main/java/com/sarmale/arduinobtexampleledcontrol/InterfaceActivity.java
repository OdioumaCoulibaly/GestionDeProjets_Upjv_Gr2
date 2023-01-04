package com.sarmale.arduinobtexampleledcontrol;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;

public class InterfaceActivity extends AppCompatActivity {

    private Button mDeconnexion,mAmoureux, mColere, mCoucou, mBaisserMain, mDanser, mTristesse, mFatigue, mTektonik, mMasque, mRire, mLeverMain, mClin_d_oeuil, mSurprise, mBase, mYoupi;
    ConnectedThread connectedThread;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_interface);


        mAmoureux = findViewById(R.id.idAmoureux);
        mColere = findViewById(R.id.idColere);
        mCoucou = findViewById(R.id.idCoucou);
        mBaisserMain = findViewById(R.id.idBaisserMain);
        mDanser = findViewById(R.id.idDanser);

        mTristesse = findViewById(R.id.idTristesse);
        mFatigue = findViewById(R.id.idFatigue);
        mTektonik = findViewById(R.id.idTektonik);
        mMasque = findViewById(R.id.idMasque);


        mRire = findViewById(R.id.idRire);
        mLeverMain = findViewById(R.id.idLeverMain);
        mClin_d_oeuil = findViewById(R.id.idClin_d_oeuil);
        mSurprise = findViewById(R.id.idSurprise);

        mBase = findViewById(R.id.idBase);
        mYoupi = findViewById(R.id.idYoupi);
        connectedThread = MyApplication.getApplication().getCurrentConnectedThread();
      //  Log.d(TAG, "");





        mAmoureux.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("1");
            }
        });
        mColere.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("2");
            }
        });
        mCoucou.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("3");
            }
        });
        mBaisserMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("4");
            }
        });
        mDanser.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("5");
            }
        });



        mTristesse.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("6");
            }
        });
        mFatigue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("8");
            }
        });
        mTektonik.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("7");
            }
        });
        mMasque.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("9");
            }
        });

        mRire.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("10");
            }
        });
        mLeverMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("11");
            }
        });
        mClin_d_oeuil.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("12");
            }
        });
        mSurprise.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("13");
            }
        });

        mBase.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("14");
            }
        });
        mYoupi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                connectedThread.write("15");
            }
        });


    }
}