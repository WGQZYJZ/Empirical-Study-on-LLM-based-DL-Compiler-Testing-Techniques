t1 = torch.mm(input_tensor_1, input_tensor_2) # Matrix multiplication between the first input tensor and second input tensor.
t2  = torch.tanh(input_tensor_3) # Apply hyperbolic tangent to each element in the first input tensor
t4 = t1 * t2 # Multiplying the first input tensor by the second output of the hyperbolic tangent function
