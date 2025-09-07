
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1 * x2], dim=0)


# Inputs to the model
input = torch.randn(4, 3, 64, 64)
mat1 = torch.randn(4, 3, 3, 64)
mat2 = torch.randn(4, 64)
