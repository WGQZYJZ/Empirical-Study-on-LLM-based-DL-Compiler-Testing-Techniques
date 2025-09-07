
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + __other__
        return v2


# Initializing the model
m = Model()
m.__other__.data.uniform_()  # Initialize the "other" tensor with uniformly distributed numbers
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
