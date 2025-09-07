
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = F.relu(v2)
        v4 = F.tanh(v3) * 6
        v5 = v4 / 6

        return v5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 90, 92)
