
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Inputs to the model
__input__  = torch.randn(1, 8, 64, 64)
v0 = __input__.view((1, 8, -1)) # (batch_size, channels, image_height * image_width)
v1 = m(__input__)
