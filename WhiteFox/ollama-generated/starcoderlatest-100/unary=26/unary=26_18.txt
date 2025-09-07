
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-6):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1) 
        self.negative_slope = torch.nn.Parameter(torch.FloatTensor([negative_slope]))

    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model and setting its parameters to different values
m = Model()
torch.nn.init.constant_(m.conv_transpose.weight[0], 0)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
