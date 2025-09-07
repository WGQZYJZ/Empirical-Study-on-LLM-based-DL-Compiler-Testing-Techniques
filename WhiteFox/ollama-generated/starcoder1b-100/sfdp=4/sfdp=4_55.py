
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(768, 768)
 
    def forward(self, x1):
        x  = self.conv(x1)
        x  = F.leaky_relu(x)
        x  = self.fc(x)
        return x


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64, dtype=torch.float)
y1 = torch.randn(768, dtype=torch.float)


