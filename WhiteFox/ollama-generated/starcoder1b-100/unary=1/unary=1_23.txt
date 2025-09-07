
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64 * 5 * 5, 8, bias=True)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model()
__input__ = m(torch.randn(1, 3, 64, 64))


