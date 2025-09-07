
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0
        v2 = (v1 * self.negative_slope).masked_fill_(mask, 0.) # Create a boolean mask where each element is True if the corresponding element in t1 is greater than zero, False otherwise
        return torch.where(mask, v1, v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
