    t1  = torch.relu(input_tensor) # Apply a ReLU transformation to the input tensor
     t2  = t1 / 4095 # Divide the output of the ReLU by 4095
     t3  = t2 + 3 # Add `3` to the output of division
