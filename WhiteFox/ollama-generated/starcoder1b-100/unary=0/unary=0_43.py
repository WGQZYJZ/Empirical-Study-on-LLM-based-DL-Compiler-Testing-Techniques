
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.avg_pool2d(x1, kernel_size=(2, 2), stride=2)
        v2 = self.conv(v1)
        v3 = v1 * 0.5
        v4 = v3 * v1
        v5 = (v4 ** 3) * 0.044715
        v6 = x1 + v5
        v7 = v6 * 0.7978845608028654
        v8 = F.tanh(v7)
        v9 = v8 + 1
        v10 = v2 * v9
        return v10


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
