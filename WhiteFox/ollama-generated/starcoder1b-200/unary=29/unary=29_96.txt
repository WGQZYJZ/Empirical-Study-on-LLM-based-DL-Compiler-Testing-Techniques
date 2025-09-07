
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.clamp_min(v1, min_value=0.5)
        v3 = torch.clamp_max(v2, max_value=0.7071067811865476)
        return v3


# Initializing the model
m = Model()
x = torch.randn(1, 8, 10, 10)
