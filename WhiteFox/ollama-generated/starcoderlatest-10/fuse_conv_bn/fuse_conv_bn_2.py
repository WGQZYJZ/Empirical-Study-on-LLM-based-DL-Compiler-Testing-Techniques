
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(2, 2, 3)

    def forward(self, x):
        output = self.conv1(x)
        return output


# Initializing the model
m = Model()
m.eval() # This is needed for FuseConvBnOptimizer to work correctly.


# Inputs to the model
x = torch.randn(2, 3, 5, 5)
output = m(x)

