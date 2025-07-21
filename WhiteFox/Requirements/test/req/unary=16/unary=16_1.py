t1 = linear(input_tensor) # Apply pointwise linear transformation to the input tensor
t2 = torch.relu(t1) # Apply the ReLU activation function to the output of the linear transformation
