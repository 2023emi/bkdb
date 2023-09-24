// Function to perform decryption in JavaScript
function decrypt(content) {
  const words = content.split(' ');
  const decryptedWords = [];

  for (const word of words) {
    const prefix = word.slice(0, 2);
    const wordWithoutPrefix = word.slice(2);
    const middle = Math.floor(wordWithoutPrefix.length / 2);
    const decryptedWord =
      wordWithoutPrefix.slice(middle) + wordWithoutPrefix.slice(0, middle);
    decryptedWords.push(decryptedWord);
  }

  return decryptedWords.join(' ');
}

// Your data array (assuming it's already loaded)
const data = [
    {
        "title": "Note 1",
        "content": "PaisTh ADsi epeth DXentcont fYfo Vqteno cQ.1 rSemLor Rtm...ipsu",
        "date": "2023-08-15",
        "tags": [
            "tag1",
            "tag2"
        ],
        "image": "https://vargiskhan.com/log/wp-content/uploads/2020/11/suraj-tal-2.jpg"
    },
    {
        "title": "Note 2",
        "content": "hCisTh Sosi ROeth wYentcont rHfo NYteno QO.2 qyemLor Itm...ipsu",
        "date": "2023-08-16",
        "tags": [
            "tag2",
            "tag3"
        ],
        "image": "image2.jpg"
    }
];


// Decrypt content for each entry in the data array
for (const entry of data) {
  if (entry.content) {
    entry.content = decrypt(entry.content);
  }
}

// Now, your data array contains decrypted content
console.log(data);
