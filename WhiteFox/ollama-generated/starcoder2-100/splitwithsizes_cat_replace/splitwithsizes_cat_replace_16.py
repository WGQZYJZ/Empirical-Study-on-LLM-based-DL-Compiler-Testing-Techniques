
# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 320, 85, 47) # Generated input tensor based on the input shape and output shape of your input image


__output__  = m(x1)

- split_tensor_dims: [1]
- split_sizes: [[4]]