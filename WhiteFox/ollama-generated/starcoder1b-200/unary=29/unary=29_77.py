
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x1, min_value=None, max_value=None):
        if min_value is None:
            min_value = torch.min(x1)
        if max_value is None:
            max_value = torch.max(x1)
 
        v1 = self.conv(x1)
        return torch.clamp(v1, min_value=min_value, max_value=max_value)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
