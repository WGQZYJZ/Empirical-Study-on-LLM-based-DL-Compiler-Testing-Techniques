
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = torch.clamp(v1, min=0.0, max=255.0)
        v3 = torch.clamp(v2, min=-127.0, max=127.0)
        return v3


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
min_value = -128
max_value = 127
