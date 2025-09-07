
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x1 = torch.cat([x1, torch.randn_like(x1), x1], dim=0)
        return self.conv(x1).sigmoid()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
