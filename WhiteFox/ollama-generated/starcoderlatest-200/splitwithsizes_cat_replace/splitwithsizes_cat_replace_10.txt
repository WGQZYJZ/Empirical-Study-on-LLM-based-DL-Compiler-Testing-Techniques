
class Model(torch.nn.Module):
    def __init__(self, num_splits=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, [num_splits], dim=-3)
        v2 = torch.cat([v[0] for v in v1])
        v4 = torch.cat([v[1] for v in v1])
        return v2, v4


# Initializing the model
m = Model(100)


# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
__output__1 = m(x1)[0] # Output of `torch.split` op should not be used as input for `torch.cat`.
__output__2 = m(x1)[1] # Output of `torch.split` op should not be used as input for `torch.cat`.


