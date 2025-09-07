
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if isinstance(other, torch.Tensor):
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if isinstance(other, torch.Tensor):
            other_tensor = other + 0.5
            print('Shape of "other" tensor:', other_tensor.shape)
        elif isinstance(other, float):
            other_tensor = torch.tensor([other]) * 0.7071067811865476 + 1.0
            print('Shape of "other" tensor:', other_tensor.shape)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if isinstance(self.other, torch.Tensor):
            v2 = v1 - self.other
        elif isinstance(self.other, float):
            v2 = v1 - self.other
        return v6


# Initializing the model
m = Model()
# Set up "other" tensor or scalar
x2 = torch.randn(1, 3, 64, 64)
m.other = x2 + 0.5


