
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        if not other_tensor:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.other_tensor = other_tensor
       
    def forward(self, x1):
        v1 = self.conv(x1)
        if not self.other_tensor:
            return v1 * 0.5
        else:
            return v1 + self.other_tensor


# Initializing the model
m = Model()

# Inputs to the model, including a tensor which is passed as keyword argument to the forward function
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8)
