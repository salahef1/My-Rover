package com.example.myrover;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

public class MainActivity extends AppCompatActivity {
    //UI Elements
    EditText textAddress;
    public static String wifiModuleIP = "";
    public static int wifiModulePort = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void connectToIP (View view){
        Intent intent = new Intent(this, ControlRoverActivity.class);
        textAddress = (EditText) findViewById(R.id.ipAddress);
        String IPandPort = textAddress.getText().toString();
        String[] tmp = IPandPort.split(":");
        wifiModuleIP = tmp[0];
        wifiModulePort = Integer.parseInt(tmp[1]);
        startActivity(intent);
    }
}