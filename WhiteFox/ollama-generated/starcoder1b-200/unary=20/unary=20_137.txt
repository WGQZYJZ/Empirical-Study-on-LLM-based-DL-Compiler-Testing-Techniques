
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x):
        v  = self.conv(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()

