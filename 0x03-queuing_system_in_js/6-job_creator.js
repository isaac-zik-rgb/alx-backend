import { createQueue } from 'kue';

const queue = createQueue();

const notifications = {
    'phoneNumber': '1234567890',
    'message': 'Hello, world!'
}

const job = queue.create('push_notification_code', notifications).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
});
