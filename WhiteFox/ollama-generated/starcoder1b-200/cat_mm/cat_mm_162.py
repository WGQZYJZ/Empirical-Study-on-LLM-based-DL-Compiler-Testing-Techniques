
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
 
    def forward(self, x):
        t1 = self.conv1(x)
        t2 = self.conv2(t1)
        return t2


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(4, 3, 64, 64)
input2 = torch.randn(4, 8, 64, 64)
