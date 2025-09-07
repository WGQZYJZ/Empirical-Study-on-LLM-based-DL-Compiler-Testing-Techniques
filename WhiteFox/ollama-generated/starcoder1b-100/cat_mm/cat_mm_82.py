
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1


# Initializing the model
m  = Model(3)


# Inputs to the model
x1  = torch.randn(4, 3, 5, 5)
x2  = torch.randn(4, 6, 5, 5)
