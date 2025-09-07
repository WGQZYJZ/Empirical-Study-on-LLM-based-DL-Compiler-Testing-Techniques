
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
        if other_tensor is not None:
            self._other_tensor = torch.nn.Parameter(
                other_tensor, requires_grad=True)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + (self._other_tensor if other_tensor is not None else 0.5)
        return v6

# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
