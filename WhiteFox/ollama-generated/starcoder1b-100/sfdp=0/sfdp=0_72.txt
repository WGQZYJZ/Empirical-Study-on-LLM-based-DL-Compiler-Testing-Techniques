
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(3, 16, 3, stride=2, padding=1)
 
    def forward(self, x):
        v = torch.cat([self.conv1(x), self.conv2(x)], dim=-1)
        v = v * 0.5
        v = v * 0.7071067811865476
        v = torch.erf(v)
        v = v + 1
        v = v * 0.25 * (v ** -0.5) # Compute the attention weights as the softmax of Scaled Dot-Product
        v = torch.cat([v, x], dim=-1)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
