
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 5, stride=2, padding=2)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t2 = (v1 > 0).float()
        v3 = torch.where((t2 * self.negative_slope), v1, v1)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 500, 500)
