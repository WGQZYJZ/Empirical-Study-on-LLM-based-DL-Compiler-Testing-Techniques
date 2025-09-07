t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * other  # Multiply a tensor or scalar "other" by the output of the convolution. This must be different from the previous value. 
t3 = torch.erf(t2) + other  # Add another tensor "other" to the output of the error function, and then apply the error function to that result
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor 
t2 = t1 - 0.5 * 3  # Subtract another constant "other" from a pointwise output by applying it to each output point and then multiplying it by a constant scalar 
t3 = torch.erf(t2) + other / other  # Add two constants, a scalar divided by itself ("other"), as well as a tensor or another scalar “other” that is the result of another multiplication operation. Then apply an error function to each output point and multiply it by its output.
