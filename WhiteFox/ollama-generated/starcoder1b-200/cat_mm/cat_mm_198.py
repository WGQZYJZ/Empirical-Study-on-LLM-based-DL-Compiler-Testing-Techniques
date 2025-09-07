
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1], dim=-1)
        return v2


# Inputs to the model
x1 = torch.randn(3, 64, 64)
x2 = torch.randn(1, 1, 64, 64)
