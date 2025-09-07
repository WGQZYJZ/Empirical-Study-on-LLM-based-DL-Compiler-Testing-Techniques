
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x, y):
        z1  = self.conv(x)
        qk = z1.matmul(y.transpose(-2, -1))
        z2 = z1.mul(torch.softmax(qk, dim=-1))
        return z2.matmul(z2)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
y = torch.randn(1, 8, 10, 10)
