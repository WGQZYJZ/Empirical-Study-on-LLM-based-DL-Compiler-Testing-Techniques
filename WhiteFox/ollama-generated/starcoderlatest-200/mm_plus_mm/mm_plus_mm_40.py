
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 5, stride=4, padding=2)
        self.conv2 = torch.nn.Conv2d(8, 16, 5, stride=3, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(1, 3, 64, 64)
input2 = torch.randn(8, 3, 1, 1)
input3 = torch.randn(8, 3, 1, 1)
input4 = torch.randn(32, 16, 10, 5)
