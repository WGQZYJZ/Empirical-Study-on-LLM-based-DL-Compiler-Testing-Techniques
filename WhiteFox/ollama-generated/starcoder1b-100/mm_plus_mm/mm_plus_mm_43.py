
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2 = torch.mm(v1, x) + v1
        v3 = torch.mm(x, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(8, 4, 64, 64)
