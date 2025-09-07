
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 5)
x2 = torch.tensor([0., -40.])
x3 = torch.randn((7, 6))

# Obtaining the outputs from the model with all inputs
outputs_all = m(x1, x2, x3)

