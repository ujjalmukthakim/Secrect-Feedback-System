import {useState} from 'react';
import { useForm } from "react-hook-form";




const Login = () => {

    const {register,handleSubmit}=useForm();



    const ItSubmit(){

    }



    return (
        <div>
            <form action="" onSubmit={handleSubmit(ItSubmit)}>
                <label htmlFor="email">
                    <span>Email</span>
                </label>
                <input
                id='email'
                type='email'
                {...register('email')}/>

            </form>
        </div>
    );
};

export default Login;