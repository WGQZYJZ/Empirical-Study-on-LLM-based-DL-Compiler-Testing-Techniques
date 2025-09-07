
class Model(nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = torch.where(v1 < 0, torch.tensor([0]), torch.tensor([1]))
        v2 = v1 * torch.neg(mask)
        return v2


# Initializing the model
m = Model()
m.negative_slope = 0.5  # Use a negative slope for the test input tensor
