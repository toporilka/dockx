import React, { useEffect, useState } from 'react';
import '../styles/Main.css'
import axios from 'axios'


function Main(){
  const [data, setData] = useState([]);


  useEffect(() => {
    axios
    .get('http://127.0.0.1:8000/user/')
    .then((Response) => {
      setData(Response.data);
    })
    .catch((Error) => {
      console.log(Error);
    });
  },
  []);
  
  
  return (
      <div>
        <div className='list_user'>
          <h1>
            List of user:
          </h1>
          <ul>
            {data.map((user) =>(
              <li key={user.id_user}>
                {user.email_user}({user.tag_user})
              </li>
            ))}
          </ul>
          <div className='login_button'>
            <button className='log_butt'><a href='/logging'>Login</a></button>
          </div>
        </div>
      </div>
  )
}

export default Main;