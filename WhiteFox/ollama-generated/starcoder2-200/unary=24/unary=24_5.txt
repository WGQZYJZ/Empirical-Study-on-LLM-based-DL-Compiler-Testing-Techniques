
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v4 = negative_slope * v1
        v5 = torch.where(v2, v1, v4)
        return v5


# Initializing the model
m = Model(negative_slope=0.3).to('cuda') # Negative slope of 0.3 is used to calculate the Leaky ReLU.

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
