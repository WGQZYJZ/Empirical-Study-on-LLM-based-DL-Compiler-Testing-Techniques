t1 = conv_transpose(input_tensor, weight) # Apply transposed convolution with kernel size 3 and stride size (2, 2), padding 0 to input tensor
t2 = t1 * 0.5  # Multiply the output of the transposed convolution by 0.5
t3 = t1 + (t1 * t1) * 0.044715  # Add the output of the transposed convolution to the output of the transposed convolution squared multiplied by 0.044715
t4 = torch.relu(t3)  # Apply relu function to the output of the previous operation
t5 = t4 * 0.7978845608028654 # Multiply the output of the previous operation by 0.7978845608028654
t6 = torch.sigmoid(t5)  # Apply sigmoid function to the output of the previous operation
t1 = batch_norm(input_tensor, weight, bias, running_mean, running_var)  # Apply batch normalization with running mean and variance computed in training mode to input tensor
t2 = t1 * 0.5 # Multiply the output of the previous operation by 0.5
