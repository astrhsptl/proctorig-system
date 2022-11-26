import React from 'react';
import { useState } from 'react';
import { redirect } from 'react-router-dom';
import AuthSystem from '../API/server';
import Links from "../UI/Links";
import classes from "./styles/Login.module.css";



const LoginComponent = ({user, setUser}) => {
  let [localData, setLocalData] = useState({
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  });

  async function getSetTokens() {
    let tokens = await AuthSystem.getTokens({
      username: localData.username, 
      password: localData.password
    });
    let login = await AuthSystem.login({
      username: localData.username, 
      password: localData.password
    });
    await setLocalData({
      username: localData.username,
      email: login.email,
      password: localData.password,
    });

    await setUser({
      id: login.id,
      username: localData.username,
      name: login.name,
      surname: login.surname,
      is_staff: login.is_staff,
      email: login.email,
      password: localData.password,
      access: tokens.access,
      refresh: tokens.refresh,
    });
  }

  return (
    <div>
      <input type="text" onChange={(e) => setLocalData({username: e.target.value, password: localData.password, access: localData.access, refresh: localData.refresh})}/>
      <input type="password" onChange={(e) => setLocalData({username: localData.username, password:e.target.value, access: localData.access, refresh: localData.refresh})}/>
      <button onClick={getSetTokens}>Send</button>
    </div>
  );
};

export default LoginComponent;