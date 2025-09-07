
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t  = torch.nn.ConvTranspose2d(16, 8, 4, stride=2)
 
    def forward(self, x1):
        v1 = self.conv_t(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 32, 64)
