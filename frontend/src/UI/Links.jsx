import React from 'react';
import { Link } from 'react-router-dom';
import { links } from '../configure/paths';
import classes from './Links.module.css';

const Links = () => {
    return (
        <div className={classes.btnTop} >
            {links.map(l =>
                    <Link to={l.path}><button className={classes.btn}>{l.pName}</button></Link>
                )}
        </div>
);

};

export default Links;