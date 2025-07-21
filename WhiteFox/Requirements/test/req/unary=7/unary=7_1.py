l1 = linear(input_tensor)  # Apply a linear transformation (pointwise linear layer) to the input tensor
l2 = linear(input_tensor)  # Apply the same linear transformation to the input tensor (used twice)
l3 = l2 + 3  # Add 3 to the output of the second linear transformation
l4 = torch.clamp_min(l3, 0)  # Clamp the result to a minimum value of 0
l5 = torch.clamp_max(l4, 6)  # Clamp the intermediate result to a maximum value of 6
l6 = l1 * l5  # Multiply the output of the first linear transformation by the clamped result
l7 = l6 / 6  # Divide the result of the multiplication by 6
