
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(3, 64, 3)
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1)
        t2 = torch.mm(t1, x1)
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        t3 = t1 + t2
        return t3 * 0.5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64, 64)
