import { createClient, print } from "redis";

const client = createClient();

client.on('connect', () => {
    console.log("Redis client connected to the server");
}
);

client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
}
);

//set hash key=value in HolbertonSchools list
client.hset('HolbertonSchools', 'Portland', '50', print);
client.hset('HolbertonSchools', 'Seattle', '80', print);
client.hset('HolbertonSchools', 'New York', '20', print);
client.hset('HolbertonSchools', 'Bogota', '20', print);
client.hset('HolbertonSchools', 'Cali', '40', print);
client.hset('HolbertonSchools', 'Paris', '2', print);

//get hash value of Portland
client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) throw err;
    console.log(reply);
}
);

