
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x):
        return torch.sigmoid(self.conv(x))


# Initializing the model
m = Model()

