

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
__output__  = m(x1)