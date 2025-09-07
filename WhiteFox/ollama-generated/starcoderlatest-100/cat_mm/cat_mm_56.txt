
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, 0 * v1])
        return v2


# Inputs to the model
x1 = torch.randn(8, 16, 3, 32)
x2 = torch.randn(8, 32, 5, 64)
