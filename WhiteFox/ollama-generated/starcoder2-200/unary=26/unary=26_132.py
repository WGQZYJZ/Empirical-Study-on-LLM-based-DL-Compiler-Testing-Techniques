
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose1d(384, 512, kernel_size=7)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 > 0).float() * torch.nn.init.normal_(torch.Tensor((512,)))
        v3 = v1 * (-0.2).cuda()
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m  = Model(-0.2).cuda()


# Inputs to the model
x1 = torch.randn(7, 56, 89)