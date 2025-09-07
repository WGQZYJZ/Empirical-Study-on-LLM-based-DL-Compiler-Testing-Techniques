
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other_tensor
        return v2

# Initializing the model with two inputs
m = Model()
other_input = torch.randn(1, 3, 64, 64)
