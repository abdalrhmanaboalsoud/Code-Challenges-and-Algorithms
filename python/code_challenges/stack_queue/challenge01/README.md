# Stack and Queue:

## Challenge01 - Implement Queue Using Stack:

<p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code> peek </code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code> pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code> peek()</code> Returns the element at the front of the queue.</li>
	<li><code> empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

## Instruction:

### Language: `JavaScript`:

* Create a branch called `stack_queue_implement_queue`.
* Run this command to pull the code challenge question: `npm run pull-challenge stack_queue 01`
* Navigate to the challenge folder: `code-challenges/stack_queue/challenge01`
* Write your solution in `challenge01.js` file.
* Write your tests in `challenge01.test.js` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `npm test`


## Language: `Python`:

* Create a branch called `stack_queue_implement_queue`.
* Run this command to pull the code challenge question: `python pull.py stack_queue 01`
* Navigate to the challenge folder: `code_challenges/stack_queue/challenge01`
* Write your solution in `challenge01.py` file.
* Write your tests in `test_challenge01.py` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `pytest`

## Language: `Java`:

* Create a branch called `stack_queue_implement_queue`.
* Run this command to pull the code challenge question: `npm run pull-challenge stack_queue 01`
* Navigate to the challenge folder: `code-challenges/stack_queue/challenge01`
* Write your solution in `App.java` file.
* Write your tests in `AppTest.java` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `gradle test`

## Submission:
* ACP your work once you are done.
* Create a pull request from your branch to the `main` branch
* Copy the link to your open pull request and paste it into the assignment submission field.
* Leave a description of how long this assignment took you in the comments box.
* Add any additional comments to your grader about your process or any difficulties you may have had with the assignment.
* Merge your branch into main, and delete your branch (don't worry, the PR link will still work).
