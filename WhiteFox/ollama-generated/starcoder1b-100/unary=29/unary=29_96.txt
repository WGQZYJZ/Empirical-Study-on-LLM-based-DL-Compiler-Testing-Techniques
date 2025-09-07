
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 3, stride=1, padding=1)
 
    def forward(self, x1, min_value, max_value):
        v1 = self.conv(x1, min_value, max_value)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 32, 32)
v1  = m(x1, 0., 5.)  # Input is clamped with min_value=0, and max_value=5.


