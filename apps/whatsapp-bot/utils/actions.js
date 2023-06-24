const fs = require('fs');
const stream = require('stream');

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


function blobToFile(blob, outputFilePath) {
  const fileWriteStream = fs.createWriteStream(outputFilePath);

  // Create a readable stream from the Blob object
  const blobStream = new stream.PassThrough();
  blobStream.end(blob.buffer);

  // Pipe the readable stream to the file write stream
  blobStream.pipe(fileWriteStream);

  return new Promise((resolve, reject) => {
    fileWriteStream.on('finish', () => {
      console.log(`File saved to ${outputFilePath}`);
      resolve();
    });

    fileWriteStream.on('error', (error) => {
      console.error('Error:', error);
      reject(error);
    });
  });
}

module.exports = { base64ToImage , blobToFile};
