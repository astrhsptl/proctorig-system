import React from 'react';
import { useEffect } from 'react';
import { useRef } from 'react';
import Webcam from "react-webcam";
import axios from "axios";
import Links from '../UI/Links';
import classes from './styles/Home.module.css';

const Camera = ({user}) => {
    function startRecording(cam, recorder, records,){
        records = [];
        recorder = new MediaRecorder(cam.current.stream, {mimeType: "video/webm"});
        recorder.start(1);
        recorder.ondataavailable = (event) => {
            records.push(event.data)
        };
        console.log(recorder)
        return {recordedData: records, mediaRecorder: recorder}
    };

    function getRecordedData(recorder, records){
        recorder.stop();
        let blob = new Blob(records, {type: 'video/webm'});
        let file = new File([blob], 'file.webm', {type: 'video/webm'} );
        return file;
    }

    function uploadFile (file) {
        console.log(file)
        let data = new FormData()
        data.append('multipart', file)
        data.append('user', user.username)
        const resp = axios({
            url: 'http://127.0.0.1:8000/stream/upl/',
            method: 'POST',
            data: data,
        });
        return resp.data
    }

    const cam = useRef();
    let recordedData =  [];
    let mediaRecorder;
    let file;
    let itr=0;

    function temp(mediaRecorder, recordedData, itr){
        mediaRecorder.stop();
        let blob = new Blob(recordedData, {type: 'video/webm'});
        let file = new File([blob], `file${itr}.webm`, {type: 'video/webm'} );
        console.log(file)
        console.log(recordedData)
        if (file.size !== 0) uploadFile(file)
    }

    useEffect(() => {
        const interval = setInterval(() =>  {
            recordedData = [];
            mediaRecorder =  new MediaRecorder(cam.current.stream, {mimeType: "video/webm"});
            mediaRecorder.ondataavailable = (event) => {
                recordedData.push(event.data)
            };
            mediaRecorder.start();
            setTimeout(temp, 5000, mediaRecorder, recordedData, itr);
            itr++;
        }, 3000)}, []);
    return (
        <div>
            <header>
                <Links></Links>
            </header>
            <div className={classes.main}>
                <Webcam mirrored={true} className={classes.web} ref={cam}></Webcam>
            </div>
        </div>
    );
};

export default Camera;