
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 4, stride=2, padding=1)
 
    def forward(self, x2):
        v2 = self.conv(x2)
        v3 = torch.sigmoid(v2)
        return v3


# Initializing the model
m = Model()

