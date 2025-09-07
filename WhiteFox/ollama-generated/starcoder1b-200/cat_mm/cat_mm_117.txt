
class Model(torch.nn.Module):
    def __init__(self, ndim: int = 2):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.mm(x1, x2)
        return torch.cat([t1, t1, ... t1])


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(1, 3, 64, 64)
