
class Model(torch.nn.Module):
    def __init__(self, other1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other1
        return v2

# Initializing the model with an additional input tensor and a keyword argument to the addition operation that will be used for performing the addition
m  = Model(other1=torch.zeros(8))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
