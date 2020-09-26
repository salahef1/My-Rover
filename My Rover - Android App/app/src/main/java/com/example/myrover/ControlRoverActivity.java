package com.example.myrover;

import androidx.appcompat.app.AppCompatActivity;

import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.WindowManager;
import android.webkit.WebView;
import android.widget.TextView;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class ControlRoverActivity extends AppCompatActivity {

    public static String wifiModuleIP = "";
    public static int wifiModulePort = 0;
    public static String CMD = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);
        setContentView(R.layout.activity_control_rover);

        wifiModuleIP = MainActivity.wifiModuleIP;
        wifiModulePort = MainActivity.wifiModulePort;
        TextView portValue = findViewById(R.id.portValue);
        TextView ipValue = findViewById(R.id.ipValue);
        portValue.setText(String.valueOf(wifiModulePort));
        ipValue.setText(wifiModuleIP);

        //Init Camera
        WebView myWebView = (WebView) findViewById(R.id.cameraWebView);
        myWebView.loadUrl("http://192.168.1.109:8081/");

        // init joystick
        JoystickView Camera_joystick = (JoystickView) findViewById(R.id.Camera_joystick);
        JoystickView Rover_joystick = (JoystickView) findViewById(R.id.Rover_joystick);
        Camera_joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            int counter = 0;
            @Override
            public void onMove(int angle, int strength) {
                if (strength != 0) {
                    Log.d("MY TEST","Moved: " + ++counter);
                    if(angle >= 45 && angle < 135){
                        moveDirection("camera_UP");
                    } else if(angle >= 135 && angle < 225){
                        moveDirection("camera_Left");
                    } else if(angle >= 225 && angle < 315){
                        moveDirection("camera_Down");
                    } else if((angle >= 315 && angle <=360) || (angle >= 0 && angle <=45)){
                        moveDirection("camera_Right");
                    }
                }
            }
        }, 1000);
        Rover_joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                if (strength != 0) {
                    if(angle >= 45 && angle < 135){
                        moveDirection("rover_UP");
                    } else if(angle >= 135 && angle < 225){
                        moveDirection("rover_Left");
                    } else if(angle >= 225 && angle < 315){
                        moveDirection("rover_Down");
                    } else if((angle >= 315 && angle <=360) || (angle >= 0 && angle <=45)){
                        moveDirection("rover_Right");
                    }
                } else {
                    moveDirection("rover_Stop");
                }
            }
        }, 600);
    }

    public void moveDirection (String direction) {
        CMD = direction;
        Socket_AsyncTask cmd_servo = new Socket_AsyncTask();
        cmd_servo.execute();
    }

    public void resetPosition (View view) {
        CMD = "camera_ResetPos";
        Socket_AsyncTask cmd_servo = new Socket_AsyncTask();
        cmd_servo.execute();
    }

    public void stopServer (View view) {
        CMD = "StopServer";
        Socket_AsyncTask cmd_servo = new Socket_AsyncTask();
        cmd_servo.execute();
    }

    public static class Socket_AsyncTask extends AsyncTask<Void,Void,Void> {
        Socket socket;

        @Override
        protected Void doInBackground(Void... params){
            try{
                InetAddress inetAddress = InetAddress.getByName(MainActivity.wifiModuleIP);
                socket = new Socket(inetAddress, MainActivity.wifiModulePort);
                DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());
                dataOutputStream.writeUTF(CMD);
                Log.d("MY TEST","DATA : " + CMD);
                dataOutputStream.close();
                socket.close();
            } catch (UnknownHostException e) {e.printStackTrace();} catch (IOException e) {e.printStackTrace();}
            return null;
        }
    }
}