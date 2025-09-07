t1 = torch.nn.functional.linear(input_tensor)  # Apply a linear transformation to an input tensor
t2 = t1 < 0                                    # Create a boolean tensor where each element is True if the corresponding element in t1 is less than 0, and False otherwise
t1 = tanh(conv_layer(input)) # Apply a hyperbolic tangent to an output of a convolutional layer applied to an input tensor
t2 = tanh(pooling(t1))  # Apply a hyperbolic tangent to an output of a max pooling operation applied on the output of applying a hyperbolic tangent function.
