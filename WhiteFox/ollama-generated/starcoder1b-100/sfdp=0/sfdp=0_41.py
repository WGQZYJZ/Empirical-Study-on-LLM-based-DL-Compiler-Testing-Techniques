
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 3, stride=2, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return torch.matmul(v2, v2.transpose(-2, -1))


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(1, 4, 64, 64)
k  = torch.randn(1, 8, 64, 64)
