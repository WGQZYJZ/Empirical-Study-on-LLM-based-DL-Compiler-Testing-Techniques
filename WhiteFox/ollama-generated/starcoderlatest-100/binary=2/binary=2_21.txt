
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_tensor = torch.ones_like(v1) # This could be a tensor of the same shape as 'v1' or a scalar
