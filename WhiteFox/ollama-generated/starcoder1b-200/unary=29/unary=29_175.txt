
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.clamp = torch.nn.functional.clamp
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x):
        v = self.conv(x)
        m = self.clamp(v, min_value, max_value)
        return m


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
