
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, 0])
        return v2


# Inputs to the model
input1 = torch.randn(8, 64, 3, 64)
input2 = torch.randn(64, 64, 1, 64)
