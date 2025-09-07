
class Model(torch.nn.Module):
    def __init__(self, x_0=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.x_0 = None
 
    def forward(self, x1, other=None):
        if not isinstance(other, Tensor):
            other = Tensor(other).contiguous().view(1, -1)
        v1 = self.conv(x1)
        return v2


# Initializing the model
m = Model()


