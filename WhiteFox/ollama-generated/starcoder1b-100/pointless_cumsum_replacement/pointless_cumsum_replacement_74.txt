
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.full([10], 1, dtype=torch.float, device=v1.device, layout=v1.layout, pin_memory=False)
        v3 = torch.cumsum(v1 * v2, dim=1)
        return v3


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
