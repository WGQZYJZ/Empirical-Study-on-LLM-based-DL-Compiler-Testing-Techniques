
model.Linear(in_features=20, out_features=4, bias=True)
model.Dropout()

# Initializing the model
m  = torch.nn.Sequential(model())

# Inputs to the model
i1  = torch.randn(32*8, 56, 70)

