t1 = linear(input_tensor) # Apply a pointwise linear transformation to the input tensor
t2 = t1 + other # Add a bias or another tensor to the output of the linear transformation
t3 = torch.relu(t2) # Apply the ReLU activation function to the result
