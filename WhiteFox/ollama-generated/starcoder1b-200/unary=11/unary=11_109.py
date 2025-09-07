
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=3, stride=2, padding=1)
 
    def forward(self, x2):
        v2 = self.conv_transpose(x2) + 3
        return torch.clamp_min(v2, 0).clamp_max(6).div_(6)


# Initializing the model
m = Model()


# Inputs to the model
__input__  = torch.randn(1, 8, 256, 256)
x2  = m(__input__)
