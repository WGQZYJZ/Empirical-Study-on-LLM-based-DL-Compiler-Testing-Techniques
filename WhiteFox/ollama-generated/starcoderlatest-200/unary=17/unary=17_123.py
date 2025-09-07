
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, 16, stride=8, padding=4)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 32, 60, 60)
