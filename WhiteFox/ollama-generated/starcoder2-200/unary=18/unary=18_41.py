t1  = conv(input_tensor)# Apply pointwise convolution with kernel size 1 to the input tensor
t2  = t1 * -0.5 # Multiply the output of the convolution by -0.5
v3  = 0 + t2# Add 0 to the output of the convolution and then multiply it by -0.5 again, yielding v3
