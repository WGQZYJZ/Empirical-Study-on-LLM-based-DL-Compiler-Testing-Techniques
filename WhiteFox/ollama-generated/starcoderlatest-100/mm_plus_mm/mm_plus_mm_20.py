
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.m2 = torch.nn.Conv2d(4, 7, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.m1(x1)
        v2 = self.m2(x1)
        v3 = torch.mm(v1, v2)
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
