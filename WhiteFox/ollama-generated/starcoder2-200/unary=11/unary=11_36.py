
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.deconv  = torch.nn.ConvTranspose2d(in_channels=8, out_channels=3, kernel_size=(50,), padding='same')
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=-6)
        v4  = torch.clamp(v3, max=60)
        v5  = v4 / 78

        return v5
