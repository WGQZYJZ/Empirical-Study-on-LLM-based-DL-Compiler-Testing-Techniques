
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(703,8)(x1) # linear transformation
        v2  = v1 + torch.randn(v1.shape[-1]) # add a random tensor of the same size to the output of the linear transformation

        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(703)


