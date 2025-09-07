
class Model(torch.nn.Module):
    def __init__(self, other: Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model with a non-zero tensor as an argument to its constructor and a random input tensor
other_tensor = torch.rand((3, 4))
m = Model(other=other_tensor)
 
x1 = torch.randn(1, 3, 64, 64)
