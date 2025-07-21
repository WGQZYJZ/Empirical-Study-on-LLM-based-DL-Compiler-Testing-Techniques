t1 = linear(input_tensor)  # Apply a linear transformation to the input tensor
t2 = linear(input_tensor)  # Apply the same linear transformation again to the input tensor

t3 = torch.sigmoid(t2)  # Apply the sigmoid function to the second output
t4 = t1 * t3  # Element-wise multiply the first linear output by the sigmoid output
