import redis from 'redis'
const { promisify } = require('util');

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const client = redis.createClient();

client.on('connect', () => {
    console.log("Redis client connected to the server");
});

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
    console.log(await setAsync(schoolName, value, redis.print));
}

async function displaySchoolValue(schoolName) {
    console.log(await getAsync(schoolName));
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');


export { client, displaySchoolValue, setNewSchool };
