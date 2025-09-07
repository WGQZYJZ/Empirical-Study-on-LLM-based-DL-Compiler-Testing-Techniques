
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = torch.sqrt(1/2)

    def forward(self, x, key):
        # ...
    def __repr__(self):
        return f'{type(self).__name__}({len(self.parameters())})'


# Initializing the model
m = Model()
key  = torch.randn(3, 512, 64, 64)
x    = torch.randn(1, 3, 64, 64)

__output__  = m(x, key)


