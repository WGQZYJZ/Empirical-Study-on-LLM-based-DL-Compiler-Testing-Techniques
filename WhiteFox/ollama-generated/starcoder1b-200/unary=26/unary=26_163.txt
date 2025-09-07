
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        m = v1 > 0 # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = torch.where(m, x1 * self.negative_slope, v1 * -1)
        return v3


# Initializing the model
m = Model()

