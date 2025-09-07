
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = v1 > 0  # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v2 = torch.where(mask, v1 * negative_slope, v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
