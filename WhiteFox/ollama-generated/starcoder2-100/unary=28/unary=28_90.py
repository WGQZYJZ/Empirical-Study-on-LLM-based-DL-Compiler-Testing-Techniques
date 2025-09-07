
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 64, 387, 389)
__output__  = m(x1)
