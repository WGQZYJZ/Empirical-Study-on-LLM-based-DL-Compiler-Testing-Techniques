
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        return v6

# Initializing the model with a tensor for "other"
m = Model(torch.ones(1, 8, 4, 4))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
