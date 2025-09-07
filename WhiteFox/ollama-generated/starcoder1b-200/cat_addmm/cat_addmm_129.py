
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 8, 1, stride=1, padding=0)
        self.fc   = torch.nn.Linear(8 * 64 * 64, 8)
 
    def forward(self, x):
        v = self.conv(x).view(x.size(0), -1)
        return self.fc(v)


# Initializing the model
m = Model()
x   = torch.randn(2, 1, 64, 64)
y   = m(x)

