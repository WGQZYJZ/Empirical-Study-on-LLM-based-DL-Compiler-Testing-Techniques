
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, x2) + inp # Performing matrix multiplication and then adding the result to another tensor 'inp'
        return v6


# Initializing the model 
m = Model()


# Inputs for the model 
x1  = torch.randn(4,3).detach().requires_grad_(True)
inp2  = torch.randn(3,) # A random input tensor

# Calculating the loss of the model 
loss  = m(x1, inp2)[0].sum()


