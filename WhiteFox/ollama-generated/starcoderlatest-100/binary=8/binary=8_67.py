
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if not isinstance(other, torch.Tensor):
            raise RuntimeError("The other tensor must be an instance of torch.Tensor")
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other 
        return v2


# Initializing the model with an instance of torch.Tensor
m = Model(other=torch.randn(1, 3, 64, 64))
