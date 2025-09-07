
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 4, 3, stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = torch.mm(v1, v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8, 3, 64, 64)
