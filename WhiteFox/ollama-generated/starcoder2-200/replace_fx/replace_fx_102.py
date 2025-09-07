
model = torch.nn.Sequential([
    torch.nn.Dropout(), # replace
    torch.nn.Linear(2, 1), # replace
    torch.nn.Tanh()   # do not erase
    ])

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(3, 1)
