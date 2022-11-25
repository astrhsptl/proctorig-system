import React, { useEffect, useState } from "react";
<<<<<<< HEAD
import { Link } from "react-router-dom";
import Links from "../UI/Links";
import classes from './styles/Home.module.css'

function HomePage({user}) {
  return (
    <div className={"Home"}> 
      <header>
        <Links></Links>
      </header>
      <div className={classes.main}>
        <div className={classes.helloText}>
          <div className={classes.mainText}>Проходите онлайн тесты и проверьте свой уровень знаний в разных направлениях.</div>
          Наш сайт предлагает Вам новейшую систему прокторинга и бесплатные прохождения тестов. <br/>
          <Link to='/login'><button className={classes.btn}>Войти</button></Link>
        </div>
        <img src={require("/home/nia/Desktop/proctorig-system/frontend/src/images/h.png")} alt="Exam" className={classes.startImage}/>
      </div>
=======
import Links from "../UI/Links";

function HomePage({user}) {
  return (
    <div className="asd"> 
    <Links></Links>
    Hello, {user.username}!
>>>>>>> 6a497cd3f17ff7985cccbe6f4b73022857b10829
    </div>
  );
}

export default HomePage;
