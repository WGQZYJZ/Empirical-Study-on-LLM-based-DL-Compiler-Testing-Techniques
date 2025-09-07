
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_up = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0)
        self.conv    = torch.nn.Conv2d(3, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv_up(x)
        v2 = torch.sigmoid(v1)
        return self.conv(v2)

# Initializing the model
m = Model()

# Inputs to the model
input  = torch.randn(1, 8, 32, 32)
