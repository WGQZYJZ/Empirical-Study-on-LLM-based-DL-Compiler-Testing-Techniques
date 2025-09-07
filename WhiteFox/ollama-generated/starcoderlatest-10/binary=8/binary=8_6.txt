
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if other is None:
            pass
        else:
          v2 = v1 + other
        return v6


# Initializing the model
m = Model()

other_tensor  = torch.randn(8, 3, 64, 64)
