t1 = batchnorm_3d(input_tensor)# Apply batch normalization to a 4D tensor.
t2 = t1 * other + 8 # Multiply 'other' from the output by some scalar, and add another constant
