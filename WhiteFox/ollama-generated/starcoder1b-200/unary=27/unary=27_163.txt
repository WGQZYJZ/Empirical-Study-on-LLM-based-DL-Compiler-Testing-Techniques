
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return torch.clamp(v1 * 0.5, min_value=min_value, max_value=max_value)


# Initializing the model
m = Model(min_value=-0.2, max_value=0.2)

