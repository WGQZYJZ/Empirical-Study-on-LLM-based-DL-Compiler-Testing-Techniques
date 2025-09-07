
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1 + 3)
        v2 = v1 - 0
        v3 = v2 / 6
        return v3


# Inputs to the model
x1 = torch.randn(1, 8, 512, 512)
