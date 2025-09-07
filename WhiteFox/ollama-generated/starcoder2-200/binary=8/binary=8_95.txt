
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + t1
        return v2


# Initializing the model
m = Model()
t1 = torch.randn(size=[4, 3, 65])

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
