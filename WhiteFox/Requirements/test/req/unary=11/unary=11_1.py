t1 = deconv(input_tensor) # Apply a deconvolution (transposed convolution) with specific kernel to the input tensor
t2 = t1 + 3 # Add 3 to the output of the deconvolution
t3 = torch.clamp_min(t2, 0) # Clamp the result from 0 and above
t4 = torch.clamp_max(t3, 6) # Clamp the result from 6 and below
t5 = t4 / 6 # Divide the result by 6
