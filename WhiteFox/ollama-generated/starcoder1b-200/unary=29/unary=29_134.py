
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2dTranspose(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.clamp_min(v, min_value)


# Initializing the model
m = Model()
