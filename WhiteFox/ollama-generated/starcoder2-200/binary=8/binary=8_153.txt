
class Model(torch.nn.Module):
    def __init__(self, other1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + other1

# Initializing the model with another tensor as keyword argument to the addition operation
m = Model(other1)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
