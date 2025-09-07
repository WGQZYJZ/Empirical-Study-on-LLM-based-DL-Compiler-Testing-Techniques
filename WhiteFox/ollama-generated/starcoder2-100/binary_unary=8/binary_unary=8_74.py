t1 = input_tensor  # Select a portion from the input tensor
t2 = t1[:, None] + other  # Concatenate another tensor onto each row in the result and add it to the output of the first convolutional layer 4th line. Please note that the first dimension here is [batch_size].
t3 = torch.relu(t2) # Apply the ReLU activation function to the result.
