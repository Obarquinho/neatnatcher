import "../css/everything.css"
import {React, useState, useEffect} from 'react'

function Post(props) {
  const [poster, setPoster] = useState("")
  const [pic, setPic] = useState("")

  /**
   * GET /api/users/<id>
   */
  const getPoster = () => {
    console.log("GET /api/users/<id>")
    fetch(props.details.poster).then(response => {
      if (response.ok) return response.json()
      else throw new Error(`${response.status} ${response.statusText}`)
    }).then(data => {
      setPoster(data.username)
      console.log(poster)
    }).catch(err => console.log(err))
  }

  /**
   * GET /api/pictures/<id>
   */
  const getPic = () => {
    console.log("GET /api/pictures/<id>")
    fetch(props.details.image).then(response => {
      if (response.ok) return response.json()
      else throw new Error(`${response.status} ${response.statusText}`)
    }).then(data => {
      setPic(data.image)
    }).catch(err => console.log(err))
  }

  useEffect(() => {
    getPoster()
    getPic()
  }, [])

  return (
    <div className="post-card">
      <img src={pic} alt="post-img"></img>
      <div className="post-text">
        <h2>{props.details.title}</h2>
        <h4>{poster}</h4>
      </div>      
    </div>
  )
}

export default Post;