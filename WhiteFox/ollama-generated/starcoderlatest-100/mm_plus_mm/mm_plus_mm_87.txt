
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(4, 16, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        t1 = torch.mm(x, x)
        t2 = torch.mm(v1, v2)
        return t3 + t4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
