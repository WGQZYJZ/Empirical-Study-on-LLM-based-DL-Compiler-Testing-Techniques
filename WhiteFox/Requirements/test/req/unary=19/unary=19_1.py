t1 = linear(input_tensor) # Apply a linear transformation to the input tensor using a pointwise operation
t2 = torch.sigmoid(t1) # Apply the sigmoid activation function to the output of the linear transformation
