const SERVER_PORT = 3001;
const URL_RE = /\%20/;

function parseURL(url) {
    return url.replace(URL_RE, ' ');
}

module.exports = {
    parseURL,
    SERVER_PORT
}