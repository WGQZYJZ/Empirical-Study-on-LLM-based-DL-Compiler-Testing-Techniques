
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(16, 8, 3, stride=2)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.sigmoid(v)


# Initializing the model
m = Model()
