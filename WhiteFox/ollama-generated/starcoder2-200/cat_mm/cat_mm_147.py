

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 5)
x2  = torch.randn(300)
__output__  = m(x1, x2)

