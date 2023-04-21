import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import Map from './Map/Map'



function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <div className="title">THIRD PLACES PROJECT</div>
      <div className='leaflet-container'>
        <Map/>
      </div> 
    </div>
    
  )
}

export default App
