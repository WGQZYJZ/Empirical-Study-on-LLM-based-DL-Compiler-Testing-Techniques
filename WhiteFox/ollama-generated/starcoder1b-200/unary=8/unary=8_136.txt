
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 4, 4, stride=2, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return v - 3


# Initializing the model
m = Model()


