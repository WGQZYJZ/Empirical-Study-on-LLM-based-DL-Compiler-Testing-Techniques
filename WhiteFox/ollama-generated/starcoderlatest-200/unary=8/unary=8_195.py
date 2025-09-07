
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1) + 3
        v2 = torch.clamp(v1, min=0, max=6)
        v3 = v1 * v2
        return v3


# Input to the model
x1 = torch.randn(1, 3, 64, 64)
