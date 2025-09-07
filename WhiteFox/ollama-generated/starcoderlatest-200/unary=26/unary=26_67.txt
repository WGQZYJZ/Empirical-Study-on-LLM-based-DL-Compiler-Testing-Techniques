
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1e-2):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 4, stride=2, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = (v1 > 0).type(torch.FloatTensor).cuda()
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64).cuda()
