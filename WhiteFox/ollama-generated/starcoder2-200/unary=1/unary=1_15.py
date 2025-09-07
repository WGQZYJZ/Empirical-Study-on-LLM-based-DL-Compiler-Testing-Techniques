
m = nn.Linear(in_features=2048, out_features=16)

# Initializing the model with randomly initialized parameters 
m()

# Inputs to the model for initialization
x3  = torch.randn(1, 512 * 7 * 7).to('cuda')
__output__  = m(x3)[0]


# Model