t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * 0.5 # Multiply the output of the convolution by 0.5
t3 = t1 + 0.784693080921842  # Add a constant value to the output of the convolution, and then 0.784693080921842 is another constant
