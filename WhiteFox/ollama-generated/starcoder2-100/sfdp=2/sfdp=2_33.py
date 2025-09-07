t1 = torch.cat((x1, x2), dim=0) # Concatenate two tensors with 4 channels by axis dimension 0
t3 = t1 * 3750 + -64  # Compute the dot product of a concatenation of two tensors and 3750; scale it by 3x10^(-2); add 3968. Subtract -64 from each element of the dot product
t4 = t3 > -4097 + torch.finfo(torch.float).eps # Check whether each element of the dot product is greater than a constant that is negative; add `eps` to each element that is less than 0 and add `eps` to all elements that are not less than 0
t5 = torch.tensor([[-43, -21], [-67, 39]]) # Create the value of the threshold tensor; this threshold value is the dot product of 1x2 and 8x2 
t6 = t3 > t5 + 1e-06  # Check whether each element of the dot product is greater than a constant that is negative plus a small number epsilon; subtract -4 from each element that is less than 0 and add -7 to all elements that are not less than 0
t9 = torch.tensor([[-21, 3], [895, -13]]) # Create the value of the threshold tensor for the second condition in the above pattern; this threshold value is the dot product of 2x4 and 7x2 
t10 = t3 < (-t9) + 1e-06  # Check whether each element of the dot product is less than a negative threshold that is greater plus a small number epsilon; subtract -8 from each element that is greater and add 5 to all elements that are not greater than 0
