import {useState} from 'react';
import { useForm } from "react-hook-form";




const Login = () => {

    const {register,handleSubmit}=useForm();



    const ItSubmit=(ok)=>{
        console.log('ok')

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
        </div>
    );
};

export default Login;