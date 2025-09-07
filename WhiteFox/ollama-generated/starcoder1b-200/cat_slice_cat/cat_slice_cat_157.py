
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.cat([x1[:, :32], x1[:, 96:]], dim=1)
        return x2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
