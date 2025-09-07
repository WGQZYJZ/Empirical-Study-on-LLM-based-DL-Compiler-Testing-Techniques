
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        w = torch.softmax(torch.matmul(x1, x2.transpose(-2, -1)), dim=-1)
        v = self.conv(x2)
        return torch.mul(w, v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
