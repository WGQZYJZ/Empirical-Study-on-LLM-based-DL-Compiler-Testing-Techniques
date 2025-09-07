
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self._register_buffer("other", other)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other
        return v2


# Initializing the model with a constant tensor as an argument to another tensor in "forward"
m = Model(torch.tensor([0]))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
