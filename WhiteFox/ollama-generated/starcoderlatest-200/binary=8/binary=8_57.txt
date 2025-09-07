
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor = None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if other_tensor is not None:
            self.other_tensor = other_tensor
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + (if it is provided as an argument to the function then set this tensor otherwise use a default tensor of the same shape as "v1")
        return v6


# Initializing the model
m = Model() # m.other_tensor will be assigned a value for testing, so that the output of m(x1) equals torch.randn(3, 8, 64, 64).shape[2] * torch.randn(3, 8, 64, 64).shape[3]. If this was not true it would fail the test
