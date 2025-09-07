

# Initializing the model
m = Model()


# Inputs to the model (the order of tensor B/A does not matter here)
x1  = torch.randn(3, 2)
x2  = torch.randn(2, 50)
__output__  = m(x1, x2)

