import "../css/everything.css"
import {useState, useEffect} from 'react'
import Post from "./post"

function Everything(props) {
  const [posts, setPosts] = useState([])  // temp: array of all posts (use context later)
  let postKey = 1                         // key for <Post>s in grid

  /**
   * GET /api/posts on page load  
   */
  const getPosts = async() => {
    console.log("GET /api/posts")    
    fetch("http://localhost:8000/api/posts/", {
      headers: {
        'Authorization': "Token c904564e406e1d17cac0191c4203a18f652941f9"
      }
    }).then(response => {
      if (response.ok) return response.json()
      throw new Error(`${response.status} ${response.statusText}`)
    }).then(data => setPosts(data.results)
    ).catch(err => console.log(err))
    
    // Sanity check: get token given django admin user/pw
    // fetch("http://localhost:8000/api-token-auth/", {
    //   method: "POST",
    //   headers: {
    //     'Content-Type': "application/json"
    //   },
    //   body: JSON.stringify({
    //     "username": "<username here>",
    //     "password": "<pw here>"
    //   })
    // }).then(response => response.json())
    // .then(data => console.log(data))
  }
  
  useEffect(() => {
    getPosts()
  }, [])

  return (
    <div className="post-grid">
      {posts.map(post => (
        <Post key={`post-${postKey++}`} details={post}  />
      ))}
    </div>
  )
}

export default Everything;