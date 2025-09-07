
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = (v1 ** 2) * 0.044715
        v3 = v1 + v2  # add the product of square and cube
        v4 = torch.tanh(v3) + 1  # add 1 to the result of tanh function
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
