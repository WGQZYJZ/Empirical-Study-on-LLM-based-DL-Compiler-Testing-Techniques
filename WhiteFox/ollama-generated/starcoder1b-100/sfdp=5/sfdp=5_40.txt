
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)
 
    def forward(self, x1, x2):
        w1  = self.conv1(x1) * math.sqrt(2/math.pi*w1.size(-1))
        w2  = self.conv2(w1) * math.sqrt(2/math.pi*w2.size(-1))
        return w2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
