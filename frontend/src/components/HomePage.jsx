import React, { useEffect, useState } from "react";
import Links from "../UI/Links";

function HomePage({user}) {
  return (
    <div className="asd"> 
    <Links></Links>
    Hello, {user.username}!
    </div>
  );
}

export default HomePage;
