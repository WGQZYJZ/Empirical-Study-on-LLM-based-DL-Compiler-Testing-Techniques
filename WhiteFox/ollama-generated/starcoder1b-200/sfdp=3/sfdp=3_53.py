
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1) * 0.5
        v2 = v1  # Zero-out the zero-point component of each input tensor except for its second dimension
        v3 = self.conv2(v2) * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (v2 * v5).mul(x2).softmax(dim=-1)
        v7 = v6.matmul(value)
        return v7


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
