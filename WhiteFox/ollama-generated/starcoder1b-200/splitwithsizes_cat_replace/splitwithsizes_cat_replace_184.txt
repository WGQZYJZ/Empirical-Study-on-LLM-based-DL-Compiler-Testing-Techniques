
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.split(v1, [1, 1], dim=1)
        v4 = [torch.nn.functional.elu(t) for t in v2]
        return torch.cat(v4, dim=1)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
