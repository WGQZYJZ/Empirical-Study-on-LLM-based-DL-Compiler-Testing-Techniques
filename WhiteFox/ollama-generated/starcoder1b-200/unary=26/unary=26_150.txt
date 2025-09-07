
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=3, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x) > 0
        return -torch.abs(v)


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 8, 64, 64)
