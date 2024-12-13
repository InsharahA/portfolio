import React from 'react';
import ReactDOM from 'react-dom';

const Greeting = ({ message }) => {
    return <h1>{message}</h1>;
};

const rootElement = document.getElementById('greeting-root');
if (rootElement) {
    const message = rootElement.getAttribute('data-message');
    ReactDOM.render(<Greeting message={message} />, rootElement);
}

ReactDOM.render(<App />, document.getElementById('app-container'));