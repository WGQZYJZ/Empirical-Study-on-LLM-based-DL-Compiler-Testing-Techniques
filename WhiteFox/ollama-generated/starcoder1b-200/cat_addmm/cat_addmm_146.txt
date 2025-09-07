
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(10, 15, 3, stride=1)
        self.fc   = torch.nn.Linear(15, 10)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x1)
        v3 = torch.cat([v1, v2], dim=-1)
        v4 = self.fc(v3)
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 10, 64, 64)
x2 = torch.randn(2, 10, 32, 32)
