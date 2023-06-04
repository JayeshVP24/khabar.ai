const fs = require('fs');

function base64ToImage(base64String, outputFilePath) {
  // Remove the data:image/<image_type>;base64 prefix
  const base64Data = base64String.replace(/^data:image\/\w+;base64,/, '');

  // Create a buffer from the base64 data
  const buffer = Buffer.from(base64Data, 'base64');

  // Write the buffer to a file
  fs.writeFile(outputFilePath, buffer, (error) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(`Image saved to ${outputFilePath}`);
    }
  });
}

module.exports = { base64ToImage };
