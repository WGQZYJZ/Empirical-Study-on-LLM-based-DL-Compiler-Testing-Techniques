
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x):
        v = self.conv(x)
        v = v + 3
        v = torch.clamp_min(v, 0)
        v = torch.clamp_max(v, 6)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8, 512, 512)
