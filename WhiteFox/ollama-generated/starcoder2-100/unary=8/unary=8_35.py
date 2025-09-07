t1  =  conv_transpose(input_tensor)# Apply pointwise transposed convolution to the input tensor 
t2  = t1 * 4 # Multiply the output of the transposed convolution by 4.
t3  =  torch.sigmoid(t2) # Apply sigmoid function to the output of the multiplication operation
t4  = t3 + 10 # Add 10 to the output of the sigmoid operation 
