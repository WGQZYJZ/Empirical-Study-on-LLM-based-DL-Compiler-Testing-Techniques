

m2  = Model()


# Inputs to the model
x1  = torch.randn(64, 3, 64, 64)
x2  = torch.randn(70, 85, 64, 9)

__output__  = m2((x1,), (x2,))

# Initializing the model
m = Model()

