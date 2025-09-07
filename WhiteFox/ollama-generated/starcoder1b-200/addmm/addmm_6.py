
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=10):
        return torch.mm(x1, x1) + inp


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
inp = 10
