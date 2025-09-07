
class Model(torch.nn.Module):
    def __init__(self, min_value: float=10e-6, max_value: float=1.0):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=0)
        self.min = min_value
        self.max = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=self.min)
        v3 = torch.clamp_max(v2, max_value=self.max)
        return v3


# Initializing the model
m = Model()


