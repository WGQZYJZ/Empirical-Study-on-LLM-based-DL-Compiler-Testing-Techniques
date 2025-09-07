
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other=None):
        v1 = self.conv(x1) + other if other is not None else v1
        return v6


# Initializing the model
m = Model()
other = torch.randn(8, 3, 4, 5)
