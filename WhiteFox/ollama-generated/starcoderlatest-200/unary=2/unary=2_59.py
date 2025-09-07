t1 = torch.max(input_tensor, dim=None) # Get the maximum element in the input tensor
t2 = t1[0]  # Use index 0 as the first dimension index to get the output value of the maximum operation
