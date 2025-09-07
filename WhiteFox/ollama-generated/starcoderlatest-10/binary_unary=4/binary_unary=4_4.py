
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor=None):
        v1 = self.conv(x1)
        if other_tensor is not None:
            v2 = v1 + other_tensor
        else:
            v2 = v1
        return torch.relu(v2)


# Initializing the model and setting its input tensor as another one with different shape from the initial input tensor.
m = Model()
x1 = torch.randn(1, 3, 64, 64)
