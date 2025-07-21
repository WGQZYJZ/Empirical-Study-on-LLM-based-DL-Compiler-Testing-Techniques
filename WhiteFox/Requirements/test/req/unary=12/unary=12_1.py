t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = torch.sigmoid(conv(input_tensor))  # Apply another pointwise convolution and then perform the sigmoid activation on its output
t3 = t1 * t2  # Multiply the output of the first convolution by the sigmoid-activated output of the second convolution
