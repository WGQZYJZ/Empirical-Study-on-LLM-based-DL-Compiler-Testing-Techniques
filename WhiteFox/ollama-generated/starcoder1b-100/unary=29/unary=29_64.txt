
class Model(torch.nn.Module):
    def __init__(self, min_value=0.354, max_value=1.262):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 2, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
