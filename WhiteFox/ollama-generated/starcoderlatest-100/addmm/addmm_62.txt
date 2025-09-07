
class Model(torch.nn.Module):
    def __init__(self, inp=None):
        super().__init__()
        if (inp is not None):
            self.inp = torch.nn.Parameter(torch.randn(1, 32))
        else:
            self.conv_t0 = torch.nn.ConvTranspose2d(16, 32, 5, stride=4)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = v1 + self.inp
        v3 = self.conv_t0(v2)
        return v3


# Input to the model and additional input tensor
x1 = torch.randn(64, 1, 64, 64)
x2 = torch.randn(64, 8, 8, 8)
