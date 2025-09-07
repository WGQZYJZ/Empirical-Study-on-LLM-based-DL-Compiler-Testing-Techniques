t1 = conv1d(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * torch.clamp(t1, min=min_value, max=max_value)  # Multiply the output of the convolution by a constant clamped to a minimum and maximum value
t1 = conv2d(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 * torch.clamp(t1, min=min_value, max=max_value)  # Multiply the output of the convolution by a constant clamped to a minimum and maximum value
t1 = conv3d(input_tensor)  # Apply pointwise convolution with kernel size (1,1,1) to the input tensor
t2 = t1 * torch.clamp(t1, min=min_value, max=max_value)  # Multiply the output of the convolution by a constant clamped to a minimum and maximum value
t1 = conv_transpose2d(input_tensor)  # Apply pointwise convolution with kernel size (1,1) to the input tensor
t2 = t1 * torch.clamp(t1, min=min_value, max=max_value)  # Multiply the output of the convolution by a constant clamped to a minimum and maximum value
t1 = conv_transpose3d(input_tensor)  # Apply pointwise convolution with kernel size (1,1,1) to the input tensor
t2 = t1 * torch.clamp(t1, min=min_value, max=max_value)  # Multiply the output of the convolution by a constant clamped to a minimum and maximum value
