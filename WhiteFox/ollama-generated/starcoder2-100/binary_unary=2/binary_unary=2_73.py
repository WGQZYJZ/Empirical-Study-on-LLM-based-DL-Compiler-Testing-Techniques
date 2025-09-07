
# Initializing the model
m  = Model()

 # Inputs to the model
other = torch.randn(8, 3, 64, 64).detach().requires_grad_()
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

