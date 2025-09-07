t1 = relu(input_tensor)  # Apply the ReLU activation function to the input tensor
t1 = tanh(input_tensor1 * input_tensor2) # Apply the hyperbolic tangent function to multiplication results obtained by multiplying two tensors.
v1 = t1 + input_tensor3  # Add a tensor to an output of the tanh function applied to the result.
t1 = relu(input_tensor) # Apply the ReLU activation function to an input tensor.
t2 = tanh(input_tensor + other_tensor)  # Apply the hyperbolic tangent function to a sum between the output of the ReLU activation function and another tensor.  
