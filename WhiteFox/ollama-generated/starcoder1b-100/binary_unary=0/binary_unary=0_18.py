
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.tensor(other)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return (v1 + self.other) * 0.5


# Initializing the model
m = Model()

