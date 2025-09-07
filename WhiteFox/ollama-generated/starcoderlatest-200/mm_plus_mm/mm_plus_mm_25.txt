
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Inputs to the model
a  = torch.randn(3, 5, 6)
b = torch.randn(7, 9, 20)
c = torch.randn(8, 2, 3)
d = torch.randn(1, 4, 5)
