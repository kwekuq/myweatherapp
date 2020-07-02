import React, {useState} from 'react';
import PlacesAutocomplete, {
    geocodeByAddress,
    getLatLng,
} from 'react-places-autocomplete';

const GoogleSearchInput = ({setGeocode}) => {
    const [address, setAddress] = useState('');

    const handleSelect = address => {
        setAddress(address)
        geocodeByAddress(address)
            .then(results => getLatLng(results[0]))
            .then(latLng => setGeocode(latLng))
            .catch(error => console.error('Error', error));
    };

    return (
        <PlacesAutocomplete
            value={address}
            onChange={setAddress}
            onSelect={handleSelect}
        >
            {({getInputProps, suggestions, getSuggestionItemProps, loading}) => (
                <div>
                    <input
                        {...getInputProps({
                            placeholder: 'Search Places ...',
                            className: 'location-search-input col-12',
                        })}
                    />
                    <div className="autocomplete-dropdown-container col-12">
                        {loading && <div>Loading...</div>}
                        {suggestions.map(suggestion => {
                            const className = suggestion.active
                                ? 'suggestion-item--active'
                                : 'suggestion-item';
                            const style = suggestion.active
                                ? {backgroundColor: '#fafafa', cursor: 'pointer'}
                                : {backgroundColor: '#ffffff', cursor: 'pointer'};
                            return (
                                <div
                                    {...getSuggestionItemProps(suggestion, {
                                        className,
                                        style,
                                    })}
                                >
                                    <span>{suggestion.description}</span>
                                </div>
                            );
                        })}
                    </div>
                </div>
            )}
        </PlacesAutocomplete>
    )
}

export default GoogleSearchInput;