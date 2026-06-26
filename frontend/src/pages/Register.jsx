// import React from 'react';
import { useForm } from "react-hook-form";

const Register = () => {

    const{register,handleSubmit}=useForm();
    const IsSubmit=(data)=>{
         console.log(data);
    }



    return (
        <div>
            <form onSubmit={handleSubmit(IsSubmit)}>
                <label htmlFor="username">
                    <span>Username</span>
                    <input type="text" 
                    id='username'
                    {...register('username')}
                    />
                </label>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default Register;