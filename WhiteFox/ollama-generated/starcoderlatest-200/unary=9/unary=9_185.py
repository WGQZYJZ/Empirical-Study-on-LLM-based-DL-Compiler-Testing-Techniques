t1 = conv(input_tensor) * 0.5 + 3 # Apply pointwise convolution with kernel size 1 to the input tensor followed by addition and clamping
t2 = torch.clamp_min(t1, 0) / 6 - 2 # Addition followed by multiplication followed by division followed by clamping with a minimum of 0 followed by a maximum of 6
out = t2 + 6 # Final addition
t1 = conv(input_tensor) * 0.5 / 3 - 1 # Apply pointwise convolution, division and clamping to the input tensor
t2 = torch.clamp_min(t1, 0) + torch.clamp_max(t1, 6) # Addition followed by multiplication followed by clamping with a minimum of 0 and maximum of 6
out = t2 / 3 + 4 # Final addition
