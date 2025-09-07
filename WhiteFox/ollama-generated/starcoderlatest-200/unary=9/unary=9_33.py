t1 = x1 + y1
t2 = conv(t1) # Apply pointwise convolution with kernel size 1 to t1 and concat the output of the previous operation and input tensor (x1 in this case) as well
t3 = t2 * 0.5 # Multiply the output of the convolution by 0.5
