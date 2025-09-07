
class Model(torch.nn.Module):
    def __init__(self, m2: torch.nn.Module):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m2 = m2
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        return self.m2(v3 + t2 + v4)


# Initializing the model
m  = Model(m2=torch.nn.ReLU())

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
