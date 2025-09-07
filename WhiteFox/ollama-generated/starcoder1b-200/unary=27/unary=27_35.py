
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1: torch.Tensor, min_value: int=0.5, max_value: int=1):
        v1 = self.conv(x1)
        v2 = v1 * min_value
        v3 = v1 * max_value
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
