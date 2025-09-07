
# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 5)
__output__  = m(x1) # The output is of shape (8, 5).

