
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15687427939910747):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=(20, 20), stride=(3, 3))
        self.relu = torch.nn.LeakyReLU()
    
    def forward(self, x1):
      v1 = self.conv(x1)
      v2 = v1 > 0
      v4 = negative_slope * (v1 - v1)
      v5 = torch.where(v2, v3, v4)
      return v5


# Initializing the model
m = Model()
negative_slope = 0.9874567983701523

# Inputs to the model
x1 = torch.randn(1, 8, 32, 32)
