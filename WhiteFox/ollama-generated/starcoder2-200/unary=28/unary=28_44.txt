

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3)
x2  = torch.randn(5, 4)
__output__  = m(x1, x2)

