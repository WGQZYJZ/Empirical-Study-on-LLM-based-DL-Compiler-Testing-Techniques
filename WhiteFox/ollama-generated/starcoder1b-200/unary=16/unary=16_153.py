
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.fc   = torch.nn.Linear(8*64*64, 8)
 
    def forward(self, x):
        v = self.conv(x).view(x.shape[0], -1)
        return self.fc(v)


# Initializing the model
m = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
