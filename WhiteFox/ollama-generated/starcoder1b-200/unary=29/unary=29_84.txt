
class Model(torch.nn.Module):
    def __init__(self, min_value=0.346895, max_value=200.7841):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp_min(v1, self.min_value), \
               torch.clamp_max(v1, self.max_value)


# Initializing the model
m = Model()


