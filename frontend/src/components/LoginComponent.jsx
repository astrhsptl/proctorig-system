import React from 'react';
import { useEffect } from 'react';
import { useState } from 'react';
import AuthSystem from '../API/server';
import Links from '../UI/Links';

const LoginComponent = ({user, setUser}) => {
  let [localData, setLocalData] = useState({
    username: '',
    password: '',
  });

  async function getSetTokens() {
    let result = await AuthSystem.getTokens({
      username: localData.username, 
      password: localData.password
    });
    await setUser({
      username: localData.username,
      email: result.email,
      password: localData.password,
      access: result.access,
      refresh: result.refresh,
    });
  }

  useEffect(() => {
    console.log(localData);
  }, [localData]) 

  return (
    <div>
      <Links></Links>
      <input type="text" onChange={(e) => setLocalData({username: e.target.value, password: localData.password,})}/>
      <input type="password" onChange={(e) => setLocalData({username: localData.username, password:e.target.value,})}/>
      <button onClick={getSetTokens}>Send</button>
    </div>
  );
};

export default LoginComponent;