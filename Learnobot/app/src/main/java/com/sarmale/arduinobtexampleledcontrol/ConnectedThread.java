package com.sarmale.arduinobtexampleledcontrol;


import android.bluetooth.BluetoothSocket;
import android.os.Handler;
import android.util.Log;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

//Class that given an open BT Socket will
//Open, manage and close the data Stream from the Arduino BT device
public class ConnectedThread extends Thread {

    private static final String TAG = "FrugalLogs";
    private final BluetoothSocket mmSocket;
    private final InputStream mmInStream;
    private final OutputStream mmOutStream;
    private String valueRead;

    public InputStream getMmInStream() {
        return mmInStream;
    }

    public OutputStream getMmOutStream() {
        return mmOutStream;
    }

    public ConnectedThread(BluetoothSocket socket) {
        mmSocket = socket;
        InputStream tmpIn = null;
        OutputStream tmpOut = null;

        // Get the input and output streams; using temp objects because
        // member streams are final.
        try {
            tmpIn = socket.getInputStream();
        } catch (IOException e) {
            Log.e(TAG, "Error occurred when creating input stream", e);
        }
        try {
            tmpOut = socket.getOutputStream();
        } catch (IOException e) {
            Log.e(TAG, "Error occurred when creating output stream", e);
        }
        //Input and Output streams members of the class
        //We wont use the Output stream of this project
        mmInStream = tmpIn;
        mmOutStream = tmpOut;
    }

    public String getValueRead(){
        return valueRead;
    }

    public void run() {

        byte[] buffer = new byte[1024];
        int bytes = 0; // bytes returned from read()
        int numberOfReadings = 0; //to control the number of readings from the Arduino

        // Keep listening to the InputStream until an exception occurs.
        //We just want to get 1 temperature readings from the Arduino
        while (numberOfReadings < 1) {
            try {

                buffer[bytes] = (byte) mmInStream.read();
                String readMessage;
                // If I detect a "\n" means I already read a full measurement
                if (buffer[bytes] == '\n') {
                    readMessage = new String(buffer, 0, bytes);
                    Log.e(TAG, readMessage);
                    //Value to be read by the Observer streamed by the Obervable
                    valueRead=readMessage;
                    bytes = 0;
                    numberOfReadings++;
                } else {
                    bytes++;
                }

            } catch (IOException e) {
                Log.d(TAG, "Input stream was disconnected", e);
                break;
            }
        }

    }
    //Write to the BT Stream

    public void write(int input) {
        //byte[] bytes = input.getBytes(); //converts entered String into bytes
        try {
            mmOutStream.write(input);
        } catch (IOException e) {
            Log.e("Send Error","Unable to send message",e);
        }
    }


    //Write to the BT Stream

    public void write(String input) {
        byte[] bytes = input.getBytes(); //converts entered String into bytes
        try {
            mmOutStream.write(bytes);
        } catch (IOException e) {
            Log.e("Send Error","Unable to send message",e);
        }
    }

    // Call this method from the main activity to shut down the connection.
    public void cancel() {
        try {
            mmSocket.close();
        } catch (IOException e) {
            Log.e(TAG, "Could not close the connect socket", e);
        }
    }
}