
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.Conv2d(8, 8, 1, stride=1, padding=0)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x2):
        v3 = self.conv_t(x2)
        v4 = self.sigmoid(v3)
        v5 = v3 * v4
        return v5

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
