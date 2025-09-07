
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(8, 16)
 
    def forward(self, x):
        v = self.conv(x)
        v = self.linear(v) + 3
        v = v / 6
        return v


# Initializing the model
m = Model()


