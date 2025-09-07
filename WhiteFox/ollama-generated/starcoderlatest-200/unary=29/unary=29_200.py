
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, 3)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = self.transposed_conv(v1)
        t2 = F.clamp(t1, min=-10, max=10)
        t3 = F.relu(t2)
        return t3


# Initializing the model
m = Model()

x1 = torch.randn(1, 3, 64, 64)
