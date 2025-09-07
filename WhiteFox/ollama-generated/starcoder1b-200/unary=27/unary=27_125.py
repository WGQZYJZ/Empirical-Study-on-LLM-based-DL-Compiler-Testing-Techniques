
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=255):
        v1 = self.conv(x1)
        return torch.clamp(v1, min=min_value, max=max_value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
min_value, max_value = 0, 255  # The value is the same as max_value in forward function
