
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor) -> None:
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._other = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other
        return v2


# Initializing the model
other_tensor = torch.randn(3,)
m  = Model(other=other_tensor)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

