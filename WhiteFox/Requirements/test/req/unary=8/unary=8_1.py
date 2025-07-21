t1 = conv_transpose(input_tensor) # Apply pointwise transposed convolution with kernel size 1 to the input tensor

t2 = conv_transpose(input_tensor) # Re-apply pointwise transposed convolution with kernel size 1 to the input tensor

t3 = t2 + 3 # Add 3 to the output of the second pointwise transposed convolution

t4 = torch.clamp_min(t3, 0) # Apply a minimum clamp of 0 to the result

t5 = torch.clamp_max(t4, 6) # Then apply a maximum clamp of 6 to the result

t6 = t1 * t5 # Multiply the output of the first transposed convolution by the clamped result

t7 = t6 / 6 # Divide the result by 6
