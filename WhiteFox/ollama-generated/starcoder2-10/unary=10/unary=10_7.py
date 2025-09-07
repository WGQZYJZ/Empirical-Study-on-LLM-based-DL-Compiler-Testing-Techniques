p  = permute(input_tensor) # Apply a permutation operation to the input tensor in order to rearrange its dimensions
t1  = conv(permute(input_tensor)) # Reapplying the pointwise convolution on the permuted output of the previous operation
t2  = t1 / 0.7846533495752335 # Divide the output of the convolution by 0.7846533495752335
