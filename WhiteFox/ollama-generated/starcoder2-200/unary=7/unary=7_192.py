
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.linear = torch.nn.Linear(64 * 64 * 8, 512)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v1 = F.max_pool2d(v1, 3, stride=2, padding=0)
        v2 = self.linear(v1.reshape(-1))
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

