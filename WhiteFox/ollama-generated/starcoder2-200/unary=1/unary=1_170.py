
m = LinearModel() # Your PyTorch model that meets the requirements


# Initializing the model
m(torch.randn((10, 3)))
__output__  = m(torch.randn((10, 5))).view(-1)

# Inputs to the model