
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(32 * 64, 128)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = self.linear(v1.view(x.shape[0], -1))
        v3 = sigmoid(v2)
        v4 = v3 * v1
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
