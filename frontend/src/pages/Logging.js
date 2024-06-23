import React, { useState } from "react";
import axios from "axios";
import { BrowserRouter as Router } from "react-router-dom";
import App from "../App";

function Logging(){
    const [data,setData] = useState({email:"",tag:""});
    const [response, setResponse] = useState("");

    const handleChange = (event) => {
        setData({...data, [event.target.name]: event.target.value });
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        axios
        .post('http://127.0.0.1:8000/login/user/', data)
        .then((response) => {
            setResponse(response.data);
        })
        .catch((Error) => {
            console.log(Error)
        });
    };

    return(
        <div>
            <h1>Logging</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    ID:
                    <input className='ID'type="text" name="id_user" value={data.id_user} onChange={handleChange}></input>
                </label>
                <br />
                <label>
                    Email:
                    <input className='Email_user'type="text" name="email_user" value={data.email_user} onChange={handleChange}></input>
                </label>
                <br />
                <label>
                    Password:
                    <input className='Password'type="text" name="password_user" value={data.password_user} onChange={handleChange}></input>
                </label>
                <br />
                <label>
                    Tag:
                    <input className='Tag' type="text" name="tag_user" value={data.tag_user} onChange={handleChange}></input>
                </label>
            </form>
            {response && (
                <p>Logging go: {response.id_user}({response.tag_user})</p>
            )}
        </div>
    )
}

export default Logging