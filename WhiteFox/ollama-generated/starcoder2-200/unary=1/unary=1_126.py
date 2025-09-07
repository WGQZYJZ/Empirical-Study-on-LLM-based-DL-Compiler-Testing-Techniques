
m  = torch.nn.Linear(64*32, 10)

# Initializing the model
m  = m()

# Inputs to the model
x1  = torch.randn(1, 64*32)
__output__  = m(x1)

