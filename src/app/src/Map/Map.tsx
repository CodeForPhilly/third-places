import './Map.css'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'


function Map() {

  return (
    <div className="leaflet-container">    
      <MapContainer center={[39.952584, -75.165222]} zoom={13} scrollWheelZoom={true}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Marker position={[39.952584, -75.165222]}>
            <Popup>
              This spots got a good vibe
            </Popup>
          </Marker>
      </MapContainer>
      </div>
  )
}

export default Map