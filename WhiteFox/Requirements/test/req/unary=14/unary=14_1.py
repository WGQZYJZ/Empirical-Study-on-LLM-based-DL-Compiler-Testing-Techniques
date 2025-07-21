t1 = conv_transpose(input_tensor)  # Apply pointwise transposed convolution to the input tensor
t2 = conv_transpose(input_tensor)  # Apply another (or the same) pointwise transposed convolution to the input tensor
t3 = torch.sigmoid(t2)  # Apply the sigmoid function to the result of the transposed convolution
t4 = t1 * t3  # Element-wise multiply the first transposed convolution output with the sigmoid output
