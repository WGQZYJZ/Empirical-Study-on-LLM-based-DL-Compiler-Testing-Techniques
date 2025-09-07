
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 3)
        self.pooling = torch.nn.MaxPool2d(kernel_size=2)
        self.conv2 = torch.nn.Conv2d(4, 8, 3)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = torch.square(v1)
        v4 = torch.cbrt(v3)
        v5 = v4 * 0.044715
        v6 = v1 + v5
        v7 = torch.pow(v6, 2.75899)
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
