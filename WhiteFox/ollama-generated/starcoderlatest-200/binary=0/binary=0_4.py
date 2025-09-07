
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor):
        v1 = self.conv(x1)
        return v1 + other_tensor


# Initializing the model
m = Model(torch.ones(20))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
