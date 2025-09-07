
class Model(torch.nn.Module):
    def __init__(self, max_value: float = 20, min_value: float = -30):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model()
