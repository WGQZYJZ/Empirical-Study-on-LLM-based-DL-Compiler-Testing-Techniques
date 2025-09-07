t1  = linear(input_tensor) # Apply a linear transformation to an input tensor
t2  = t1  # Return True if each element in the output is negative, False otherwise
t3  = t2  > 0  # Return True for each element where both elements from previous layer and input are greater than zero. Otherwise return False
t4  = -t1  + 1  # For each element that is positive, set its value to be the inverse of its corresponding element in the input; otherwise, do not modify its original value
t5  = t2 if t3 else t4  # For each element where both elements from previous layer and input are greater than zero, set its value as the inverse of its correponding element in the input. Otherwise return the original value
t1 = torch.tanh(input_tensor)  # Apply hyperbolic tangent to each element in an input tensor
t2 = torch.sqrt(torch.sum(v2 * v3, dim=[0], keepdim=True))  # Compute the square root of the sum over the elements in t1 with respect to dimension 0 and return a new tensor. The square root is then applied to each element.
t1 = torch.sigmoid(input_tensor)  # Apply sigmoid function to each element in an input tensor
t2 = torch.sigmoid(torch.abs(v3))  # Compute the absolute value of v4, then apply the sigmoid function to it and return the result. The output is a boolean mask where each element is True if its corresponding element from the input was negative, False otherwise. This mask will be used in a later step for the final output.
t3 = t1  > 0.5 # Compute a boolean mask indicating whether each element of the input tensor is greater than 0.5. This mask will also serve as an index to pick out elements from v4 during the calculation of a nonlinearity (ReLU) and add a constant offset in another later step
v3 = t1 * -2  # Multiply each value by minus 2. The result is used for applying a non-linearity, such as ReLU in another later step.
t6  = v4 + torch.abs(0.5)  # Add the input to the nonlinaer operation (ReLU). For each element where the mask was True during the previous step and where each value from v2 was negative, add 1/2. For those elements where t3 was False and their values were positive, add a negative half of itself. The results is then added to another constant in a later step
