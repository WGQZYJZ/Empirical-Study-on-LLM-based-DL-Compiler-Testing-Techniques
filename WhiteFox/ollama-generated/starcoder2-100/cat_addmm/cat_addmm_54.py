t1 = torch.zeros((m, n)) + 4 # Initialize a vector with shape (n,) and assign it to 4.0
t2 = t1  / 3 # Divide each element in the vector by 3.
t3 = torch.softmax(t2, dim=0) # Apply softmax along dimension 0 on each element of the vector. 
