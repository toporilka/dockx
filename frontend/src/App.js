import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './styles/App.css';
import Logging from "./pages/Logging";
import Main from "./pages/Main";

function App(){
  return(
    <BrowserRouter>
    <div className="navbar">
      <div className="navbar__links">
        <a href="/logging">Logging</a>
      </div>
    </div>
      <Routes path="/logging">
        <Route>
          <Logging/>
        </Route>
      </Routes>
      <Routes path="/Main">
        <Main />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
