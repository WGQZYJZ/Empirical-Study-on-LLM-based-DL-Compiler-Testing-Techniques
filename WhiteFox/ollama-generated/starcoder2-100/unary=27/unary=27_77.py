t1 = conv(input_tensor)# Apply pointwise convolution with kernel size 1 to the input tensor
t2 = max(t1, 0.5)# Take the maximum of the output of the convolution and a constant value `0.5`
t3 = min(max(t2), 4.5) # Take the minimum between the maximum operation and another constant `4.5`
