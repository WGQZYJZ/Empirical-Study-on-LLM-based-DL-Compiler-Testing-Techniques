
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3) # Use padding=1 to achieve convolution with kernel size equal to the number of channels in the previous layer multiplied by a constant 3
        self.conv2 = torch.nn.Conv2d(8, 64, 1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = v2 * 0.5
        v4 = (v3 + (v3 * v3 * v3) * 0.044715) * 0.7978845608028654
        v5 = torch.tanh(v4)
        v6 = v5 + 1
        v7 = v2 * v6
        return v7


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
