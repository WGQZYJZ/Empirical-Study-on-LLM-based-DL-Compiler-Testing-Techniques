
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v6

 # Inputs to the model
x1 = torch.randn(10000, 10000)
x2 = torch.randn(10000, 10000)
inp = torch.randn(10000)
