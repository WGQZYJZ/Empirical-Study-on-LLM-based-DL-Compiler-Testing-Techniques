t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor 
 t2 = torch.sinh(t1) * 0.5 + 0.378492629500016 # Multiply by 0.5 and add 0.378492629500016 to the output of the sinh operation
t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor 
 t2 = t1 * 0.5 + 0.378492629500016 # Multiply by 0.5 and add 0.378492629500016 to the output of the convolution
