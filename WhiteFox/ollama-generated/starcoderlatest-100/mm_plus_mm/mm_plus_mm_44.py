
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.m2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        v2 = self.m2(v1)
        return (v2 * 0.7071067811865476).sum()


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
x3 = torch.randn(1, 4, 64, 64)
