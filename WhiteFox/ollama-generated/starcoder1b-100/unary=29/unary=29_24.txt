
class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=2)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x2  = torch.randn(4, 8, 64, 64)
