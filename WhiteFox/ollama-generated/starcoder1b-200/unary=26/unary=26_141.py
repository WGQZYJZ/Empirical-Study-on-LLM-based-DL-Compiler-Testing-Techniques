
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
        self.leakyrelu = nn.LeakyReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0
        v2 = -negative_slope * (v1)
        v3 = self.leakyrelu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 10, 10)
