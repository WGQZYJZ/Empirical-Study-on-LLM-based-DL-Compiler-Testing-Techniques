
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=3, stride=1)
 
    def forward(self, x1, min_value=-10.0, max_value=10.0):
        v1 = self.conv(x1, min_value=min_value, max_value=max_value)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
