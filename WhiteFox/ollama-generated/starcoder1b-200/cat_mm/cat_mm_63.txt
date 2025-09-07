
class Model(nn.Module):
    def __init__(self, m1=None, m2=None):
        super().__init__()
        self.m1 = nn.Conv2d(3, 8, 1, stride=1, padding=1) if m1 is None else m1
        self.m2 = nn.Conv2d(8, 32, 3, stride=2, padding=1) if m2 is None else m2
 
    def forward(self, x1, x2):
        return torch.cat([self.m1(x1), self.m2(x2)], dim=1)


# Initializing the model
m = Model()
m1 = nn.Conv2d(3, 8, 1, stride=1, padding=1)
m2 = nn.Conv2d(8, 32, 3, stride=2, padding=1)


