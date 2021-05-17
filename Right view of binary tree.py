
def rightView(root):
    if not root:
        return
    queue=[]
    queue.append(root)
    while queue:
        l=len(queue)
        while l:
            temp=queue[0]
            if l==1:
                print(temp.data,end=" ")
            l-=1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            queue.pop(0)
