
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(3, 128, 4)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3
        return torch.clamp(v1, min=0, max=6) / 6


# Inputs to the model
x1 = torch.randn(1, 128, 50, 50)
