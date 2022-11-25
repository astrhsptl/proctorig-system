import React from 'react';
import classes from './LocalInput.module.css';

const LocalInput = ({type, placeholder}) => {
    return (
        <input type={type} placeholder={placeholder} className={classes.inp}/>
    );
};

export default LocalInput;