
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.02):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, 4)
        self.negative_slope = torch.tensor(negative_slope)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.functional.leaky_relu(v1, negative_slope=self.negative_slope)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 16, 16)
