
class Model(torch.nn.Module):
    def __init__(self, other=20):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.tensor(other, dtype=torch.float)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return self.other + v1


# Initializing the model
m = Model()

