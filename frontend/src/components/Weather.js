import React from 'react';
import {Line} from "react-chartjs-2";

const Weather = ({weather}) => {
    return (
        weather !== {} ? (
            <div className="grid-container">
                <div className="graph">
                    <Line data={weather.hourly_temperatures}
                          options={{
                              maintainAspectRatio: true,
                              responsive: true,
                              aspectRatio: 1,
                              redraw: true
                          }}
                          height={120}
                    />

                </div>
                <div className="temp">
                    <p><strong>Min Temperature: </strong>{weather.min_temp}</p>
                    <p><strong>Max Temperature: </strong>{weather.max_temp}</p>
                    <p><strong>Average Temperature: </strong>{weather.avg_temp}</p>
                    <p><strong>Median Temperature: </strong>{weather.median_temp}</p>
                </div>
                <div className="humidity">
                    <p><strong>Min Humidity: </strong>{weather.min_humidity}</p>
                    <p><strong>Max Humidity: </strong>{weather.max_humidity}</p>
                    <p><strong>Average Humidity: </strong>{weather.avg_humidity}</p>
                    <p><strong>Median Humidity: </strong>{weather.median_humidity}</p>
                </div>
            </div>) : null
    )
}
export default Weather;