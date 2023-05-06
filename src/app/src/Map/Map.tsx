import './Map.css'
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import Button from 'react-bootstrap/Button';


function Map() {
  const buttonStyle = {backgroundColor:"#ADD8E6", marginLeft: '1rem', marginRight: '1rem'}
  return (
    <div className="leaflet-container-wrapper">
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
      <div className="button-container">
        <Button style={buttonStyle} variant="primary">Near Me</Button>
        <Button style={buttonStyle} variant="primary">On the Way To</Button>
        <Button style={buttonStyle} variant="primary">Around Destination</Button>
      </div>
    </div>
  )
}

export default Map