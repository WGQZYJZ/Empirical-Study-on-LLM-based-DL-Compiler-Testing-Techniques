t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 + negative_slope # Add the negative slope to the output of the convolution
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * negative_slope # Multiply the output of the convolution by the negative slope
t3 = t2 + negative_slope_for_activation # Add the negative slope for activation to the result of the multiplication
