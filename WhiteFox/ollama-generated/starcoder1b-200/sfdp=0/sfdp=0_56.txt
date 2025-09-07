
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x1.transpose(-2, -1)) / math.sqrt(torch.size(v1)[0] * torch.size(v1)[1])
        v3 = torch.matmul(v1, x1)
        v4 = torch.exp(-math.pow(v3, 2) / 2) / math.factorial(torch.size(v3)[0])
        return v2 * v4


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
