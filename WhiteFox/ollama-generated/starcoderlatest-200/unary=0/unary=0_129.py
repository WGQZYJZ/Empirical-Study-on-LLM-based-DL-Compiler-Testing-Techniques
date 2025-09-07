
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = v1 * 0.5
        v4 = v1 * v1
        v5 = v4 * v1
        v6 = v5 * 0.044715
        v7 = v3 + v6
        v8 = torch.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10


# Initializing the model
m = Model()

 # Inputs to the model
x = torch.randn(1, 3, 64, 64)
