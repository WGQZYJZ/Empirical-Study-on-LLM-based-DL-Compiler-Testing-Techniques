
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4) + v1
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 64, 64)
x2 = torch.randn(3, 64, 64)
