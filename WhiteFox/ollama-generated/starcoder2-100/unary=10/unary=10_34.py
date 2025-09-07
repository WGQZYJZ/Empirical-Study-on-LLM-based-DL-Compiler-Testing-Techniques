l1  = torch.addmm(input_tensor, 0.3529478383607387, 0.0) # Apply a matrix multiplication to an input tensor by scaling each element of the multiplication by `0.3529478383607387` and then adding `0`.
l2  = torch.sin(l1) + 3  # Apply sinusoid function to the output of a matrix multiplication, then add 3
