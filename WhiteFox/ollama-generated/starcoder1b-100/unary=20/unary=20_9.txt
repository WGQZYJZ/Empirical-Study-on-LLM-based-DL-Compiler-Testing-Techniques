
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1, stride=2, padding=0)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()


