t1 = conv(input_tensor, bias=None)  # Apply pointwise convolution without bias to the input tensor. The bias parameter is not specified.
v2 = t1[0][4] + t1[3][7] + t1[6][8] + t1[5][9]   # Compute the sum of the elements at positions (0, 4), (3, 7), (6, 8) and (5, 9).
