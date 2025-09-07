
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2 = v1 - other # Other is a scalar.
        return v2

m  = Model()
# Inputs to the model
x = torch.randn(1, 3, 64, 64)

