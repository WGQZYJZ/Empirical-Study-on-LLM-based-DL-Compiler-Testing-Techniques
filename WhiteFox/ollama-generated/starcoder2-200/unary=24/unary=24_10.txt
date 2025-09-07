
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.5):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).to(torch.float32) # Create a boolean mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3  = v1 * self.negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model with negative slope of 0.5
m = Model()

