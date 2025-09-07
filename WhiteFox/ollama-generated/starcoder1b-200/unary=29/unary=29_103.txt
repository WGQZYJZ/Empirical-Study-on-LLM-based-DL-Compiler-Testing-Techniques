
class Model(torch.nn.Module):
    def __init__(self, min_value, max_value):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1, min_value, max_value):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, self.min_value)  # Clamp the output of the convolution to a minimum value
        v3 = torch.clamp_max(v2, self.max_value)  # Clamp the output of the previous operation to a maximum value
        return v3


# Initializing the model
m = Model(min_value=10, max_value=90)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
