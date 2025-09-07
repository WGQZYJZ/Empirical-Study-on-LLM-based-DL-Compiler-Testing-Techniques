
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 10, 3)
 
    def forward(self, x):
        v4 = (self.conv * (x + x)).mean([0, 2, 3])
        return v4
