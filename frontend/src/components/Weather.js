import React from 'react';

const Weather = ({weather}) => {
    return (
         weather !== {} ? (
        <div className="grid-container">
            <div className="graph">

            </div>
            <div className="temp">
                <p><strong>Min Temperature: </strong>{weather.min_temp}</p>
            </div>
            <div className="humidity">

            </div>
        </div>) : null
    )
}
export default Weather;