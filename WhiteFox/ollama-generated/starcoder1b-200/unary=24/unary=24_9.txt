
class Model(nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1)
        self.negative_slope = negative_slope

    def forward(self, x):
        mask = x > 0
        positive_component = x * self.negative_slope
        negative_component = torch.where(mask, x, positive_component)
        return torch.cat([positive_component, negative_component], dim=1)

# Initializing the model
m = Model()


