t1 = linear(input_tensor)  # Apply a linear transformation (pointwise linear layer) to the input tensor
t2 = torch.clamp_min(t1, min_value)  # Clamp the result of the linear transformation at a minimum value
t3 = torch.clamp_max(t2, max_value)  # Clamp the aforementioned result to a maximum value
