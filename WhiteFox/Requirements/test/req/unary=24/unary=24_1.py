t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 > 0  # Compare the output of the convolution to 0
t3 = t1 * negative_slope  # Multiply the output of the convolution by a `negative_slope` parameter
t4 = torch.where(t2, t1, t3)  # Select elements from `t1` or `t3` based on the comparison in `t2`
