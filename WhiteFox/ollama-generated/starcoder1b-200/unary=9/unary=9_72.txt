
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + 3  # Add the constant 3 to the output of the convolution
        return torch.clamp_min(v1, 0), torch.clamp_max(v1, 6) / 6


# Initializing the model
m = Model()


