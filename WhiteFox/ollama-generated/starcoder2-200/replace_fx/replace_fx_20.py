

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 2) # For dropout
x2  = torch.randn(32, 50) # For randlike

__output__  = m(x1)

