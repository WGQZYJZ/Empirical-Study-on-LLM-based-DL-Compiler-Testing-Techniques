
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(16, 32, 2, stride=2)
        self.fc   = torch.nn.Linear(10, 16)
 
    def forward(self, x):
        v = F.relu(self.conv(x))
        return torch.sigmoid(self.fc(v))

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
