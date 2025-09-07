
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1) * 0.5
        v3 = (v1 ** 2) * 0.7071067811865476
        v4 = (v3 ** 3) * 0.044715
        v5 = v1 + v4
        v6 = v5 * 0.7978845608028654
        return torch.tanh(v6)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
