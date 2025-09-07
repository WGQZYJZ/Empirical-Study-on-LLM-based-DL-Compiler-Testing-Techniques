
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=0.125) * 1000
        v3 = torch.clamp_max(v2, max_value=1.0625) * 1000
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
kwargs = {'min_value': 0.125, 'max_value': 1.0625}
