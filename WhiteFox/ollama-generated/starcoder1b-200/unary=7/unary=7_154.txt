
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        l1 = torch.nn.functional.linear(v1, clamp(min=0, max=6, v1 + 3)) # Multiply the output of the linear transformation by the clamped output of the linear transformation added with 3
        v2 = l1 / 6
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
