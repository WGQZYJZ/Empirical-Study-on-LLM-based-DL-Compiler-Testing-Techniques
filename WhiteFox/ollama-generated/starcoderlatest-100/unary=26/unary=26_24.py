
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(16, 32, 4, stride=4, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        t1 = (v1 > 0).float()
        negative_slope = torch.nn.Parameter(torch.zeros_like(v1), requires_grad=True)
        v3 = v1 * negative_slope
        v4 = torch.where(t1, v1, v3)
        return v4


# Inputs to the model
x1 = torch.randn(1, 16, 256, 256)
