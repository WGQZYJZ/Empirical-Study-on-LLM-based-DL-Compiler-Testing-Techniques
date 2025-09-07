
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 5)
        self.conv2 = torch.nn.Conv2d(4, 20, 3)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) * 0.964
        v2 = torch.mm(v1, self.conv2(x2)) + 0.5
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 128, 128)
x2 = torch.randn(1, 4, 128, 128)
