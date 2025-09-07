
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Inputs to the model
x1 = torch.randn(64, 512)
x2 = torch.randn(64, 512)
x3 = torch.randn(512, 64)
x4 = torch.randn(512, 64)
