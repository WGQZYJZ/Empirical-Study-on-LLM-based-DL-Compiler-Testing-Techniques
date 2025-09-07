

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2, 3)

# Initializing the initial parameters for the model
negative_slope  = -0.5 

__output__   = m(x1, negative_slope=negative_slope)

