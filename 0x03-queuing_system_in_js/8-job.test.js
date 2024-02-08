import { describe, it, before, after, afterEach } from "mocha";
import { expect } from "chai";
import { createQueue } from "kue";

import { createPushNotificationsJobs } from "./8-job";

import createPushNotificationsJobs from "./8-job";

const queue = createQueue();

describe("createPushNotificationsJobs", function () {
  before(function () {
    queue.testMode.enter();
  });

  after(function () {
    queue.testMode.exit();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  it("createPushNotificationsJobs", function () {
    createPushNotificationsJobs(queue);
    expect(queue.testMode.jobs.length).to.equal(10);
  });
  it("Test wether jobs are created correctly", function () {
    createPushNotificationsJobs(queue);
    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_2");
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
    });
    it('display an error message if jobs is not an array', function() {
        expect(() => createPushNotificationsJobs('string', queue)).to.throw('Jobs is not an array');
    });

    it('Test whether jobs are created', function() {
        const jobs = [
            {
              phoneNumber: '4153518780',
              message: 'This is the code 1234 to verify your account'
            },
            {
              phoneNumber: '4153518781',
              message: 'This is the code 4562 to verify your account'
            },
            {
              phoneNumber: '4153518743',
              message: 'This is the code 4321 to verify your account'
            }
          ];
          reatePushNotificationsJobs(jobs, queue);

          expect(queue.testMode.jobs.length).to.equal(2);
      
          expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
          expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
      
          expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
          expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
        });
    });
