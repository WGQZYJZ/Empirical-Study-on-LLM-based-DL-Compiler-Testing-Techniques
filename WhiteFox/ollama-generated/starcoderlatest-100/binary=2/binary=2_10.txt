
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if isinstance(other, torch.Tensor):
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            assert type(other) is float or type(other) is int
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if isinstance(self.conv, torch.nn.Conv2d):
            other = torch.randn_like(v1)
            v2 = v1 - other
        else:
            assert type(self.conv) is float or type(self.conv) is int
            other = self.conv 
            v2 = v1 - other

        return v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.tensor(-0.5)
