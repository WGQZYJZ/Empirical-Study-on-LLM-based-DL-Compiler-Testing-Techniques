
# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8, 320, 64) # Input tensor for the first torch.split call
x2  = x1[:, ::2]               # Indexing to split the input along axis=1 by half the length of each sub-tensor created by the split operation
__output__   = m(x1, x2)

