// import {useState} from 'react';
import { useForm } from "react-hook-form";
import API from "../api";
import {Link} from 'react-router-dom'




const Login = () => {

    const {register,handleSubmit}=useForm();



    const ItSubmit=(data)=>{
        API.post('login/',data).then((res)=>{
            console.log(res.data)
            console.log(res.data.token)
        }).catch((err)=>{
            console.log(err)
        })

        // console.log(data)

    }



    return (
        <div>
            <form action="" onSubmit={handleSubmit(ItSubmit)}>
                <label htmlFor="username">
                    <span>Username</span>
                </label>
                <input
                id='username'
                type='text'
                {...register('username')}/>

                <label htmlFor="password">
                    <span>Password</span>
                </label>
                <input
                id='password'
                type='password'
                {...register('password')}/>
                <button type='submit'>Submit</button>

                

            </form>
            <Link to="/register">Register</Link>
        </div>
    );
};

export default Login;