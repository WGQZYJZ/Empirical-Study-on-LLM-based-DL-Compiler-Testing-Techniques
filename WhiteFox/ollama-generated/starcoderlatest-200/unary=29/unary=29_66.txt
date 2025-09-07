
class Model(torch.nn.Module):
    def __init__(self, min_value=0.5, max_value=0.7):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp(v1 * 0.5, min_value, max_value)
        v3 = torch.clamp(v2 * 0.7071067811865476, min_value, max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
