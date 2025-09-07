t1 = batch_norm(input_tensor)  # Apply batch normalization to the input tensor
t2 = max_pool(t1, kernel_size=3)  # Apply max pooling with a kernel size of three to the output of the batch normalization.
t3 = average_pool(t1, kernel_size=7)  # Apply average pooling with a kernel size of seven to the output of the batch normalization.
