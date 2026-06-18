import {useState} from 'react';
import { useForm } from "react-hook-form";




const Login = () => {

    const {register,handleSubmit}=useForm();



    const ItSubmit(){

    }



    return (
        <div>
            <form action="" onSubmit={handleSubmit(ItSubmit)}>

            </form>
        </div>
    );
};

export default Login;