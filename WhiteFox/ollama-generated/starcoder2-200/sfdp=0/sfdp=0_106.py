t1_relu  = tanh(add + mul) # Apply hyperbolic tangent to a tensor by performing element-wise addition and multiplication with another tensor. This model is an example for hyperbolic tangent function.
t2  = conv1d_2(input) # Apply a 1D convolution to the input, which is 3-dimensional. The resulting output will be of size 10-by-50.
t3  = conv1d_2(input).softmax() # Apply a 1D convolution to the input followed by softmax operation, resulting in an output with 10 rows and five columns.
t4  = torch.nn.ReLU()(t1) + t2  # Addition is performed by applying element-wise addition between two tensors. The output of this model is the sum of hyperbolic tangent output plus convolutional layer output.
