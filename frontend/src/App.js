import React, { useState } from 'react';
import './styles/App.css';

function App(){
  const [value, setValue] = useState('text_to_input')



  return(
    <div className='App'>
      <div className='post'>
        <div className='post_content'>
          <strong>1. Java</strong>
          <div>
            Java govno
          </div>
        </div>
        <div className='post_button'>
          <button>Fact</button>
        </div>
      </div>
    </div>
  );
}

export default App;


