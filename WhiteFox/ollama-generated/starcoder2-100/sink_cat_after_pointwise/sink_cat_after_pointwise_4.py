

# Initializing the model
model  = torch.nn.Linear(3, 1)

# Inputs to the model
__input1__  = torch.randn(20)
__input2__  = torch.ones(20).to(__input1__.device)

