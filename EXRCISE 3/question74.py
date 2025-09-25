stack=[];
stack.append("lecture 1");
stack.append("Lecture 2");
stack.append("Lecture 3");
print(stack);
stack.pop();
stack.pop();
stack.pop();
print("poped all",[stack]);

stack=[];
stack.append("formA");
stack.append("formB");
stack.append("formC");
print(stack);
stack.pop();
print("undo one, remained is",[stack]);

stack=[];
stack.append("1");
stack.append("2");
stack.append("3");
print(stack);
stack.pop();
stack.pop();
print(stack);
stack.append(4);
print("which is on the top is 4 seemly",stack);
# 1.at RRaA 5 client queue. after 1 served, who is front
queue=[];
queue.append("C1");
queue.append("C2");
queue.append("C3");
queue.append("C4");
queue.append("C5");
print(queue);
queue.remove(queue[0]);
print(queue);
# 2. at RSSB 7 client queue. who is third served?
queue=[];
queue.append("C1");
queue.append("C2");
queue.append("C3");
queue.append("C4");
queue.append("C5");
queue.append("C6");
queue.append("C7");
print("served third ",queue[2]);


