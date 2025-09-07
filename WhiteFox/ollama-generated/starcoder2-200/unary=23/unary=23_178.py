
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__  = m(x1)

# References: 
https://pytorch.org/docs/stable/nn.html#torch.nn.ConvTranspose2d
https://pytorch.org/docs/stable/nn.html#tanh
