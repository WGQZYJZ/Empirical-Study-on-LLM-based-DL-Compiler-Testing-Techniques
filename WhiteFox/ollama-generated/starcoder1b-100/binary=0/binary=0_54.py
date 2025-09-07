
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other is not None:
            self.other = torch.nn.Parameter(torch.Tensor([1]))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return (v1 + self.other).view_as(x1)


# Initializing the model
m = Model()


