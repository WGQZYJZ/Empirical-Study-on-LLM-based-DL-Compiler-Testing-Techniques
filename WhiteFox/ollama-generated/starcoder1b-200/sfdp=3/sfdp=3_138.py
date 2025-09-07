
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(in_features=8 * 64 * 64, out_features=32 * 7 * 7)
 
    def forward(self, x):
        v  = self.conv1(x)
        v = torch.flatten(v, 1)
        v = self.fc(v)
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
