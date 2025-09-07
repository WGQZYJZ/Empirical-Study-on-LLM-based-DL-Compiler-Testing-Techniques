t1 = conv(input_tensor) # Apply a convolution on the input tensor
t2 = t1 * 4 + 6 # Multiply the output of the convolution by 4 and add 6 to it
t3 = torch.sigmoid(t2)# Apply sigmoid function to the output of the previous multiplication operation plus addition operation, and then apply a threshold to the resulting tensor with values above 0.5
t1 = linear(input_tensor)# Apply a linear transformation to an input tensor
t2 = t1  * 0.5 # Multiply the output of the previous linear transformation by 0.5
t3 = 4 + 6# Add 4 and 6 to the output of the multiplication operation
