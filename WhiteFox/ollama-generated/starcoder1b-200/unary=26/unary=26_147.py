
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
        self.relu = torch.nn.LeakyReLU()
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1 > 0) * (self.negative_slope)
        v3 = self.conv(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(2, 3, 64, 64)
