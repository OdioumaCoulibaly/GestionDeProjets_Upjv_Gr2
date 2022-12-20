package com.example.learnobot;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.annotation.SuppressLint;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.UUID;

public class  MainActivity extends AppCompatActivity {

    private Button  mDeconnexion, mColere, mCoucou, mBaisserMain, mDanser, mEffraye, mFatigue, mFaim, mTournerBassin, mHeureux, mLeverMain, mPleurer, mSurprise, mTournerTete, mYoupi;

    //-------------------------------------------
    Handler bluetoothIn;
    final int handlerState = 0;
    private BluetoothAdapter btAdapter = null;
    private BluetoothSocket btSocket = null;
    private StringBuilder DataStringIN = new StringBuilder();
    private ConnectedThread MyConexionBT;
    // Identificador unico de servicio - SPP UUID
    private static final UUID BTMODULEUUID = UUID.fromString("00001101-0000-1000-8000-00805F9B34FB");
    // String para la direccion MAC
    private static String address = null;
    //-------------------------------------------
    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        bluetoothIn = new Handler() {
            public void handleMessage(android.os.Message msg) {
                if (msg.what == handlerState) {
                    //Interacción con los datos de ingreso
              /*      char MyCaracter = (char) msg.obj;

                    if (MyCaracter == 'a') {
                        tvtMensaje.setText("ACELERANDO");
                    }

                    if (MyCaracter == 'i') {
                        tvtMensaje.setText("GIRO IZQUIERDA");
                    }

                    if (MyCaracter == 'd') {
                        tvtMensaje.setText("GIRO DERECHA");
                    }

                    if (MyCaracter == 'r') {
                        tvtMensaje.setText("RETROCEDIENDO");
                    }

                    if (MyCaracter == 's') {
                        tvtMensaje.setText("DETENIDO");
                    }*/
                }
            }
        };

        btAdapter = BluetoothAdapter.getDefaultAdapter();
        VerificarEstadoBT();
        //-----------------------------------------------------------------------



        mColere = findViewById(R.id.idColere);
        mCoucou = findViewById(R.id.idCoucou);
        mBaisserMain = findViewById(R.id.idBaisserMain);
        mDanser = findViewById(R.id.idDanser);
        mDeconnexion = findViewById(R.id.idDeconnexion);

        mEffraye = findViewById(R.id.idEffraye);
        mFatigue = findViewById(R.id.idFatigue);
        mFaim = findViewById(R.id.idFaim);
        mTournerBassin = findViewById(R.id.idTournerBassin);


        mHeureux = findViewById(R.id.idHeureux);
        mLeverMain = findViewById(R.id.idLeverMain);
        mPleurer = findViewById(R.id.idPleurer);
        mSurprise = findViewById(R.id.idSurprise);

        mTournerTete = findViewById(R.id.idTournerTete);
        mYoupi = findViewById(R.id.idYoupi);






        mColere.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mColere");
            }
        });
        mCoucou.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mCoucou");
            }
        });
        mBaisserMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mBaisserMain");
            }
        });
        mDanser.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mDanser");
            }
        });



        mEffraye.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mEffraye");
            }
        });
        mFatigue.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mFatigue");
            }
        });
        mFaim.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mFaim");
            }
        });
        mTournerBassin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mTournerBassin");
            }
        });

        mHeureux.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mHeureux");
            }
        });
        mLeverMain.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mLeverMain");
            }
        });
        mPleurer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mPleurer");
            }
        });
        mSurprise.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mSurprise");
            }
        });

        mTournerTete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mTournerTete");
            }
        });
        mYoupi.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MyConexionBT.write("mYoupi");
            }
        });


        mDeconnexion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (btSocket != null) {
                    try {
                        btSocket.close();
                    } catch (IOException e) {
                        Toast.makeText(getBaseContext(), "Error", Toast.LENGTH_SHORT).show();
                        ;
                    }
                }
                finish();
            }
        });

    }


    //xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    private BluetoothSocket createBluetoothSocket(BluetoothDevice device) throws IOException {
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
        }
        return device.createRfcommSocketToServiceRecord(BTMODULEUUID);
        //creates secure outgoing connecetion with BT device using UUID
    }

    @Override
    public void onResume() {
        super.onResume();

        Intent intent = getIntent();
        address = intent.getStringExtra(DispositifConnecter.EXTRA_DEVICE_ADDRESS);
        //Setea la direccion MAC
        BluetoothDevice device = btAdapter.getRemoteDevice(address);

        try {
            btSocket = createBluetoothSocket(device);
        } catch (IOException e) {
            Toast.makeText(getBaseContext(), "La création de la Socket a échoué", Toast.LENGTH_LONG).show();
        }
        // Establece la conexión con el socket Bluetooth.
        try {
            if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                // TODO: Consider calling
                //    ActivityCompat#requestPermissions
                // here to request the missing permissions, and then overriding
                //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                //                                          int[] grantResults)
                // to handle the case where the user grants the permission. See the documentation
                // for ActivityCompat#requestPermissions for more details.
                btSocket.connect();
                //Toast.makeText(getBaseContext(), "CONEXION EXITOSA", Toast.LENGTH_SHORT).show();

                //return;
            }

            //btSocket.connect();
        } catch (IOException e) {
            try {
                btSocket.close();
            } catch (IOException e2) {
            }
        }
        MyConexionBT = new ConnectedThread(btSocket);
        MyConexionBT.start();
    }

    @Override
    public void onPause() {
        super.onPause();
        try { // Cuando se sale de la aplicación esta parte permite que no se deje abierto el socket
            btSocket.close();
        } catch (IOException e2) {
        }
    }

    //Comprueba que el dispositivo Bluetooth
    //está disponible y solicita que se active si está desactivado
    private void VerificarEstadoBT() {

        if (btAdapter == null) {
            Toast.makeText(getBaseContext(), "El dispositivo no soporta bluetooth", Toast.LENGTH_LONG).show();
        } else {
            if (btAdapter.isEnabled()) {
            } else {
                Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
                if (ActivityCompat.checkSelfPermission(this, Manifest.permission.BLUETOOTH_CONNECT) != PackageManager.PERMISSION_GRANTED) {
                    // TODO: Consider calling
                    //    ActivityCompat#requestPermissions
                    // here to request the missing permissions, and then overriding
                    //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                    //                                          int[] grantResults)
                    // to handle the case where the user grants the permission. See the documentation
                    // for ActivityCompat#requestPermissions for more details.
                    startActivityForResult(enableBtIntent, 1);
                    //return;
                }

            }
        }
    }

    //Crea la clase que permite crear el evento de conexion
    private class ConnectedThread extends Thread
    {
        private final InputStream mmInStream;
        private final OutputStream mmOutStream;

        public ConnectedThread(BluetoothSocket socket)
        {
            InputStream tmpIn = null;
            OutputStream tmpOut = null;
            try
            {
                tmpIn = socket.getInputStream();
                tmpOut = socket.getOutputStream();
            } catch (IOException e) { }
            mmInStream = tmpIn;
            mmOutStream = tmpOut;
        }

        public void run()
        {
            byte[] byte_in = new byte[1];
            // Se mantiene en modo escucha para determinar el ingreso de datos
            while (true) {
                try {
                    mmInStream.read(byte_in);
                    char ch = (char) byte_in[0];
                    bluetoothIn.obtainMessage(handlerState, ch).sendToTarget();
                } catch (IOException e) {
                    break;
                }
            }
        }

        //Envio de trama
        public void write(String input)
        {
            try {
                mmOutStream.write(input.getBytes());
            }
            catch (IOException e)
            {
                // s'il n'est pas possible d'envoyer des données, la connexion est fermée
                Toast.makeText(getBaseContext(), " La connexion a échoué", Toast.LENGTH_LONG).show();
                finish();
            }
        }
    }
    //xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
}



