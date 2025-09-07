t2 = relu(t1) # Applying the ReLU function to the output of the linear transformation 
t3 = maxpool(t2, kernel_size=kernel_size) # Applying the 2D max pooling operation to the output of the ReLU activation function with a specified window size.
