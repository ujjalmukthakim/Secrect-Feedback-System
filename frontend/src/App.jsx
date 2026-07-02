// import { useState } from 'react'

import './App.css'
import Login from './pages/Login'
import Register from './pages/Register'
import {Link} from 'react-router-dom'

function App() {
  // const [count, setCount] = useState(0)

  return (
    <div>
      <Login/>
      <Link to="/register">Register</Link>
 
      
    {/* <Register/> */}
    </div>

  )
}

export default App
