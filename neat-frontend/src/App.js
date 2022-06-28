import logo from './logo.svg';
import './App.css';
import Everything from './components/everything'
import Navbar from './components/navbar'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import {React, useState, useEffect} from 'react'

function App() {
  const [isDesktop, setIsDesktop] = useState(window.innerWidth > 890) // whether browser window is desktop width

  useEffect(() => {
    /**
     * Set isDesktop on resize
     */
    let resizeListener = window.addEventListener("resize", () => {
      setIsDesktop(window.innerWidth > 890)
    });
    return () => {
      window.removeEventListener("resize", resizeListener);
    }
  });


  return (
    <Router>
      <Navbar isDesktop={isDesktop} />
      {/* Look through children <Route>s in <Routes> and render first 
      match with current URL  */}
      <Routes>
        <Route path="/" element={<Everything />} />
      </Routes>
    </Router>
    
  );
}

export default App;
