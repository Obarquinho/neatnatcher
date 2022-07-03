import "../css/page.css"

function Page(props) {
  return (
    <div className="page-container">
      <h1>{props.title}</h1>
      {props.content}
    </div>
  )
}

export default Page;