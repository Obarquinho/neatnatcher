import "../css/navbar.css"
import bars from "../assets/bars-solid.svg"
import close from "../assets/rectangle-xmark-regular.svg"
import { useEffect, useState } from "react"

function Navbar(props) {
  const [showLinks, setShowLinks] = useState(false) // whether nav links are displayed
  let linksStyle = props.isDesktop ?                // inline styles for nav links
    {
      flexDirection: "row"
    } 
    : {
      flexDirection: "column", 
      justifyContent: "center",
      boxSizing: "border-box",
      position: "absolute", 
      top: "0",
      right: "0",
      background: "var(--brown)",
      width: "100%",
      height: "100vh", 
      padding: "15px 20%", 
      opacity: showLinks ? "1" : "0"
    } 

  /**
   * Hide/show nav links on btn click on mobile
   */
  const toggleLinks = () => {
    setShowLinks(!showLinks)
  }

  return (
    <header>
      <a href="/">Neat Natcher</a>
      {!props.isDesktop ? 
        showLinks ? <img onClick={toggleLinks} src={close}></img>
          : <img onClick={toggleLinks} src={bars}></img> 
        : <></>}      
        <div className="nav-links" style={linksStyle}>          
          <a href="/">Posts</a>
          <a href="/users">Users</a>
          <a href="/">Map</a>
          <button href="/">Sign Up</button>        
        </div>      
    </header>
  )  
}

export default Navbar;