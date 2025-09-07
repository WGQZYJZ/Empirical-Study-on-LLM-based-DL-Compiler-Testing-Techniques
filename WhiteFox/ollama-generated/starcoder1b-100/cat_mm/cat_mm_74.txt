
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return torch.cat([v1, v1], dim=1)


# Inputs to the model
input1  = torch.randn(2, 8, 64, 64)
input2  = torch.randn(3, 8, 64, 64)
