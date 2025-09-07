
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.tconv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=1, output_padding=(0, 0), groups=8)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.tconv(v1)
        return v2


# Initializing the model
m = Model()

