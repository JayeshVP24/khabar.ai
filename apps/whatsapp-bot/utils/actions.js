var urlRegex = /(https?:\/\/[^\s]+)/g;

/**
 * 
 * @param {string} input 
 * @returns {string}
 */
const isUrl = (input) => {
    const url =  input.match(urlRegex);
    if (url !== null) {
        return true
    } 
    return false
}



// const firstMessage = `
// Hello, I am a bot that can help you with your queries.
// Press 1 to enter a query.
// Press 2 to enter a fact check an article link.
// `

module.exports = {isUrl}