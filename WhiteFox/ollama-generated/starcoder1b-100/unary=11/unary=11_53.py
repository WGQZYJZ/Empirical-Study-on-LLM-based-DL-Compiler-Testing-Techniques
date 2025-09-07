
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = v1 + 3
        v3 = torch.clamp(v2, 0, 6)
        v4 = torch.clamp(v3 / 6, 0, 255)
        return v4


# Initializing the model
m = Model()


