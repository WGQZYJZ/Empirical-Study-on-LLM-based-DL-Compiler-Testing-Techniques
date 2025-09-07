

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(2, 8) # Initialize a 2 by 8 tensor with normal distribution. 
x3 = m(x1).detach().numpy()

