import React from "react";
import './styles/App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route, 
  Link
} from 'react-router-dom'
import Logging from "./pages/Logging";
import Main from "./pages/Main";
import './styles/App.css'
import {ReactComponent as Key} from './styles/key.svg'
import {ReactComponent as Main_svg} from './styles/main.svg'

function App(){

 return(
    <Router>
    <div className="navbar">
      <nav>
        <div className="navbar__links">
          <ul className="navbar_menu">
            <li className="navbar_item">
              <Link to = "/Logging" className="navbar_link"><Key></Key></Link>
            </li>
            <li className="navbar_link">
              <Link to = "/Main" className="navbar_link"><Main_svg></Main_svg></Link>
            </li>
          </ul>
        </div>
      </nav>
      <Routes>
        <Route path="/Logging" element={<Logging />}>
        </Route>
        <Route path="/Main" element = { <Main />}>
        </Route>
      </Routes>
    </div>
    </Router>
  );
}


export default App;
