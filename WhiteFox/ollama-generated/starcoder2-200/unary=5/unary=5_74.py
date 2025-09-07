t1  = pointwise_linear(input_tensor) # Apply pointwise linear operation to the input tensor
t2 = t1 * t1  # Square the output of the pointwise linear operation (e.g., the first layer of an MLP)
t3 = t1 + 0.5 # Add half 1 to the output of the pointwise linear operation
