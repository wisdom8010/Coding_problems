def LeftView(root):
    if not root:
        return
    queue=[]
    queue.append(root)
    while queue:
        l=len(queue)
        p=l
        while l:
            temp=queue[0]
            if l==p:
                print(temp.data,end=" ")
            l-=1
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            queue.pop(0) 
