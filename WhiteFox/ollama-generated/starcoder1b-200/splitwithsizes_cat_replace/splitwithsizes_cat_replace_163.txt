
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return True if any([
            isinstance(x, torch.Tensor)
            and x.dim() == 4
            for x in [
                self.conv(x1),
                *torch.split(x1, (2, 0, 1)),
                *torch.cat([self.conv(x1), *torch.split(x1, (1, 0, 3))]),
            ]
        ]) else False


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
