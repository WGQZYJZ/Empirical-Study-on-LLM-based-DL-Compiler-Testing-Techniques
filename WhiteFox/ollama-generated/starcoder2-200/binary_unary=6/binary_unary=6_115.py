
# Initializing the model
m  = Model()

 # Inputs to the model
other_tensor = torch.randn(batch, 256).requires_grad_()
x1  = torch.randn(batch, 256)
