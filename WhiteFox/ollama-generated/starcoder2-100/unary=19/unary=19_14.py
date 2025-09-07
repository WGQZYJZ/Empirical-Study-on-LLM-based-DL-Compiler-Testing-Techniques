

# Initializing the model
m = nn.Linear(784, 5)

# Inputs to the model
x = torch.rand((32, 784))
__output__  = m(x)

