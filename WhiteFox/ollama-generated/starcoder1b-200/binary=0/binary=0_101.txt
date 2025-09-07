
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_tensor = other_tensor

    def forward(self, x1):
        v1 = self.conv(x1) + self.other_tensor
        return v1


# Initializing the model
m = Model(other_tensor=torch.randn(2, 3, 64, 64))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
