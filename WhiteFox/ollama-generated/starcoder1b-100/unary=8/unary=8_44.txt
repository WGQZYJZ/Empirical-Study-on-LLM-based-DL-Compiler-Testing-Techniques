
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x2):
        v5 = self.conv(x2)
        return v5 / 6


# Inputs to the model
x2 = torch.randn(2, 3, 64, 64)
