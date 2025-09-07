
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.conv2 = torch.nn.Conv2d(8, 64, kernel_size=5)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.7978845608028654
        v3 = torch.tanh(v2)
        v4 = v3 + 1
        v5 = self.conv2(v4)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
