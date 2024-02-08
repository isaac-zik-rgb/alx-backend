function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');
  jobs.forEach((job) => {
    const jobData = {
      phoneNumber: job.phoneNumber,
      message: job.message
    };
    const jobQueue = queue.create('push_notification_code_2', jobData).save((err) => {
      if (!err) console.log(`Notification job created: ${jobQueue.id}`);
    });
    jobQueue.on('complete', () => {
      console.log(`Notification job ${jobQueue.id} completed`);
    }).on('failed', () => {
      console.log(`Notification job ${jobQueue.id} failed`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${jobQueue.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
