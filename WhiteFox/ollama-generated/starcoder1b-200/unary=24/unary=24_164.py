
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        mask = x1 > 0  # Create a boolean mask where each element is True if the corresponding element in t1 is greater than 0, False otherwise
        v1 = self.conv(x1) * mask
        v2 = v1 * negative_slope
        return torch.where(mask, v1, v2)


# Initializing the model
m = Model()


