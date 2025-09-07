
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1[:, :, :32] + v1[:, :, 32:] # Slice the input along dimension 1
        v3 = torch.cat([v1[:, :, :32], v2], dim=1) # Concatenate the original input and sliced tensor along dimension 1
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
