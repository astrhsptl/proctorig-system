import React from 'react';
import { redirect } from 'react-router-dom';
import Links from '../UI/Links';

const SelfPage = ({user}) => {
    if (user.is_staff !== true) {
        return redirect('/login');
      }
    return (
        <div>
            <Links></Links>
            {user.username}, 
        </div>
    );
};

export default SelfPage;