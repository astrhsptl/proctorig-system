import React, { useEffect, useState } from "react";
import {BrowserRouter,Outlet,Route, Routes,} from "react-router-dom";
import { paths } from "./configure/pages";


function App() {
  let [user, setUser] = useState({
    id: '',
    name: '',
    surname: '',
    is_staff: false,
    username: '',
    email: '',
    password: '',
    access: '',
    refresh: '',
  });

  useEffect(() => {
    console.log(user) 
  }, [user])

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          {paths.map(route => 
            <Route path={route.path} element={<route.component user={user} setUser={setUser}/>}/>
          )}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;