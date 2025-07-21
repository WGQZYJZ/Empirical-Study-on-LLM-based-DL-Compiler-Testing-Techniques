l1 = linear(input_tensor)  # Apply a pointwise linear transformation (linear layer with kernel size 1) to the input tensor
l2 = l1 * 0.5  # Multiply the output of the linear transformation by 0.5
l3 = l1 * 0.7071067811865476  # Multiply the output of the linear transformation by 0.7071067811865476
l4 = torch.erf(l3)  # Apply the error function to the output of the linear transformation
l5 = l4 + 1  # Add 1 to the output of the error function
l6 = l2 * l5  # Multiply the scaled output of the linear transformation by the output of the error function plus 1
