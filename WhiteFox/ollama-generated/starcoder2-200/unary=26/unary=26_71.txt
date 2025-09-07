
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(32, 8, 5, stride=2)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model()
negative_slope = 0.1

 # Inputs to the model
x1  = torch.randn(1, 32, 57, 98)
