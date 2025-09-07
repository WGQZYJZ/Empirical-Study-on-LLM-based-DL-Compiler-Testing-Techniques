
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other
        v4 = torch.relu(v2)
        return v4


# Initializing the model
m = Model()
m._other = m.conv.weight  # _other is another tensor to add with conv.weight; it can be a random tensor or a known value that will not affect the analysis results.
m(x1).sum().backward()

