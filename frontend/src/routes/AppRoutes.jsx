// import React from 'react';
import {Routes,Route} from 'react-router'
import Login from '../pages/Login'
import Register from '../pages/Register';
import App from '../App'

const AppRoutes = () => {
    return (
        <Routes>
            <Route element={<App/>}/>
            <Route path='/login' element={<Login/>}/>
            <Route path='/register' element={<Register/>}/>
        </Routes>

    );
};

export default AppRoutes;