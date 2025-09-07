t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor, followed by Batch Normalization and ReLU layers
t2 = t1 * 0.5  # Multiply the output of the convolution by a constant
v3 = v1 + other  # Add another tensor to the output of the convolution
t1 = conv(input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 + other  # Add another tensor to the output of the convolution, and then multiply both the outputs of the convolution by a constant. The "other" tensors is passed as a keyword argument to the addition operation.
