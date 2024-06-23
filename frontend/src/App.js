import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React from 'react';

class App extends React.Component{
  state = {details: [], }
  componentDidMount(){
    let data;
    axios.get('http://127.0.0.1:8000/api/client')
    .then(res =>{
      data = res.data
      this.setState({
        details:data
      });
    })
    .catch(err =>{
      console.log(err)
    })
  }
  render(){
    return(
      <div>
        <header>
          Data from Django
        </header>
        <hr></hr>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <div>
              <h2>{output.id_client}</h2>
              <h3>{output.name_client}</h3>
              <h3>{output.second_name_client}</h3>
              <h3>{output.status}</h3>
              <h3>{output.id_user}</h3>
            </div>
          </div>
        ))}
      </div>
    )
  }
}
export default App;
