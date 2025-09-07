
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.full([x1.size()[0], 1], 1, dtype=torch.float64, layout=torch.strided, device="cpu", pin_memory=False)
        v2 = self.conv(x1) * v1
        v3 = torch.cumsum(v2, dim=1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
