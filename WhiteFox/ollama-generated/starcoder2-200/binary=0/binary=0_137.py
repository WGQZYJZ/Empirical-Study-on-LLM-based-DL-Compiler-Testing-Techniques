
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # v1 and "other" are not the same tensor. They must be treated as two different tensors.
        return v2

# Initializing the model
m  = Model(torch.randn(3,8))

