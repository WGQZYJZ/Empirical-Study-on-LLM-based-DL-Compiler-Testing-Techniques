t1 = conv(input_tensor) # Apply pointwise convolution with kernel size 2 to the input tensor. Here, the kernel size is larger than one; in this case, it is `2` for `2`D data.
t2 = t1 + t1  # Add t1 twice because the 0.5 constant in a multiplication operation will not be considered.
