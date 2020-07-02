import React, {useEffect, useState} from "react";
import {render} from "react-dom";
import axios from 'axios';
import GoogleSearchInput from "./GoogleSearchInput";
import Weather from './Weather'

const App = () => {
    const [latLng, setLatLng] = useState({});
    const [weather, setWeather] = useState({});
    useEffect(() => {
        const params = {
            'lat': latLng.lat,
            'lng': latLng.lng
        }
        if (latLng !== {} ) {
            axios.get('/api/v1/weather/', {params: params})
                .then(res => {
                    setWeather(res.data)
                })
                .catch(console.log)
        }
    }, [latLng])

    return (
        <>
            <div className="text-center">
                <form className="form-search">
                    <h1 className="h3 mb-3 font-weight-normal">Search for City</h1>
                    <GoogleSearchInput setGeocode={setLatLng}/>
                </form>
                <Weather weather={weather}/>
            </div>
        </>
    )
}

export default App;

const container = document.getElementById("app");
render(
    <App/>
    , container);