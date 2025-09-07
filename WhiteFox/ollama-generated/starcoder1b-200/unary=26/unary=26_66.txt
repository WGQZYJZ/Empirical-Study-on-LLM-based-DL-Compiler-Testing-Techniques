
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v2 = v1 * self.negative_slope
        v3 = torch.where(mask, x1, v2)
        return v3


# Initializing the model
m = Model(-0.5)


