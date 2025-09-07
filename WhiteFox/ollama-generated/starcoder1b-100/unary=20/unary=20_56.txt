
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, kernel_size=1, stride=2)
 
    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


