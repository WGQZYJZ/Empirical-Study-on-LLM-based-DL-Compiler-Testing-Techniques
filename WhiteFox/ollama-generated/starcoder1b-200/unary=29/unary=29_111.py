
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=1):
        v1 = self.conv(x1)
        return v1  # Return the output of the convolution


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
v1 = m(x1)
min_value = -3
max_value = 3
