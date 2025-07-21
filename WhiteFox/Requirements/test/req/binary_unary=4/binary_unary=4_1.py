t1 = linear(input_tensor)  # Apply a pointwise linear (fully connected) operation to the input tensor
t2 = t1 + other_value      # Add a constant or another tensor called "other" to the output of the linear operation
t3 = torch.relu(t2)        # Apply the ReLU activation function to the result of the addition
