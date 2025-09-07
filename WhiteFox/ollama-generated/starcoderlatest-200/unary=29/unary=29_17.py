
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 1, stride=1, padding=1)
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 1, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1 * 0.5, min_value)
        v3 = torch.clamp_max(v2 * 0.7071067811865476, max_value)
        return self.conv_transpose(v3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 224, 224)
