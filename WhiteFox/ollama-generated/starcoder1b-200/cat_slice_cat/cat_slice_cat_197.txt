
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, x1):
        v0 = torch.cat([x0[:, :256], x0[:, 257:]], dim=1)
        v1 = torch.cat([x1[:, :256], x1[:, 257:]], dim=1)
        return v1 - v0


# Inputs to the model
x0 = torch.randn(3, 3, 256, 256)
x1 = torch.randn(3, 3, 256, 256)
