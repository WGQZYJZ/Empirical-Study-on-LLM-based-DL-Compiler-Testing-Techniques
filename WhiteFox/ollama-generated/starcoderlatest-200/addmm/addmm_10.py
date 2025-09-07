
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + inp

 # Inputs to the model and keyword arguments
inp = torch.randn(16, 32)
x1 = torch.randn(4, 16, 8, 8)
x2 = torch.randn(4, 16, 8, 8)
