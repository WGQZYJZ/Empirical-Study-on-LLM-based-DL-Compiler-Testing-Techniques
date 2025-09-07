t1  = conv(input_tensor) # Apply pointwise convolution with kernel size 1 to the input tensor
t2 = t1 > 0 # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
t3 = t1 * negative_slope # Multiply the output of the convolution by the negative slope
t4 = torch.where(t2, t1, t3) # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
