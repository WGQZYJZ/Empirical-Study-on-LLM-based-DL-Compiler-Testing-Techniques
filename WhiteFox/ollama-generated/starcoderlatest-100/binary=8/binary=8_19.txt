
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other if other is not None else v1
        return v2


# Initializing the model with a given tensor to add
other_tensor = torch.randn(1, 3, 64, 64)
m = Model(other=other_tensor)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
