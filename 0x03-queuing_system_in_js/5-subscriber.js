import { createClient } from "redis";

const client = createClient();

//connect to the server
client.on('connect', () => {
    console.log("Redis client connected to the server");
}
);

//error handling
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err}`);
}
);

client.subscribe('holberton school channel');

//listen for messages on channel and print message when rercieved
client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        client.unsubscribe(channel);
        client.quit();
    }
}
);
