# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(50, 8, 64, 64)
other = np.random.randn(1,)
 
# Outputs of the model on these inputs
__outputs__ = m(x1)
 
