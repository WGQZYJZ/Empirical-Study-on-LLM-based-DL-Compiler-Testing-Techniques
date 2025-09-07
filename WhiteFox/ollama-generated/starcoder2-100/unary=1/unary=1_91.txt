

# Initializing the model
m  = LinearTransformation(in_features=32)

# Inputs to the model
x1 = torch.randn(8, 32)
__output__  = m(x1)