
class Model(torch.nn.Module):
    def __init__(self, input_shape):
        super().__init__()
        self.conv = torch.nn.Conv2d(input_shape[1], 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).detach()
        v2 = v1 > 0
        v3 = v1 * -0.7
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model((3, 64, 64))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
