
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x1, x2, x3, x4):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.mm(v2, x3)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(1, 8, 32, 32)
input3 = torch.randn(1, 16, 8, 8)
input4 = torch.randn(1, 8, 40, 40)
