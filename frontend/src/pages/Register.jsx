// import React from 'react';
import { useForm } from "react-hook-form";
import API from "../api";

const Register = () => {

    const{register,handleSubmit}=useForm();
    const IsSubmit=(data)=>{
         console.log(data);
         API.post('',data).then((res)=>console.log(res.data))
    }



    return (
        <div>
            <form onSubmit={handleSubmit(IsSubmit)}>
                <label htmlFor="rusername">
                    <span>Username</span>
                    <input type="text" 
                    id='rusername'
                    {...register('username')}
                    />
                </label>

                <label htmlFor="rpassword">
                    <span>Password</span>
                    <input type="password"
                    id="rpassword"
                    {...register('password')} />


                </label>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Register;