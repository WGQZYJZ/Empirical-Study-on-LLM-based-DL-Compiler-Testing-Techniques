t1  = max(input_tensor) # Apply the maximum operation on a 3D tensor with the shape [N, C, H] to the input tensor. The input tensor can have any shape.
t2  = tanh(t1) # Apply the hyperbolic tangent function to the output of the maximum operation
