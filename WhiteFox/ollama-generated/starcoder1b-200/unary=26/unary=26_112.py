
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v3 = negative_slope * v1
        v4 = torch.where(v2, x1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(1, 8, 64, 64)
