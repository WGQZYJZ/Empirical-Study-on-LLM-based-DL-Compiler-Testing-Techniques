
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if isinstance(other, (torch.Tensor, int)) or isinstance(other, float):
            other_tensor = torch.full((3,), value=other, dtype=x1.dtype)
            self.other = other_tensor
        else:
            self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1) - self.other
        return v1


# Initializing the model
m = Model()
