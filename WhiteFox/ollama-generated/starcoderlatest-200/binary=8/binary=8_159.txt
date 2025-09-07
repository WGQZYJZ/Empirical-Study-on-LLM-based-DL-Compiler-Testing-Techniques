
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_tensor = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other_tensor
        return v6


# Initializing the model and passing another tensor as an input
m = Model(torch.ones((1, 3, 64, 64)))
