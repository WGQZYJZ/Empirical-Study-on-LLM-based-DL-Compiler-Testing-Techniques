t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = tanh(t1) * 0.5 + 0.498039216 # Apply hyperbolic tangent function to the output of the convolution, then add `0.498039216` to obtain the value of 50% of the hyperbolic tangent, and finally multiply by `0.5`.
