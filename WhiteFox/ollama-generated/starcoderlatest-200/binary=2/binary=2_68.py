
class Model2(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_tensor = other_tensor
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - self.other_tensor
        return v2


# Initializing the model
m2 = Model2(torch.randn(3))

