
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        other_tensor = x1 * 0.5 + v1 * 0.7071067811865476
        return other_tensor

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other_tensor = x1 * 0.5 + x1 * 0.7071067811865476
