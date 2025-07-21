t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to input tensor
t2 = t1 + other # Add another tensor or a constant to the output of the convolution
t3 = torch.relu(t2) # Apply the ReLU (Rectified Linear Unit) function to the result
