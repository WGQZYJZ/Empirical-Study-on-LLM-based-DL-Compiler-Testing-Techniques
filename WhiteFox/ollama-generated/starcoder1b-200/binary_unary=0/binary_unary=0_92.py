
class Model(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(dim, 32)
 
    def forward(self, x1):
        x = self.conv(x1)
        x = x + __other__
        return self.fc(x)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
