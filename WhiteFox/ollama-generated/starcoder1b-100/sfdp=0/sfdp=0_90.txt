
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc    = torch.nn.Linear(8, 4)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        w1 = v3 * 0.5
        w2 = w1 * w1

        w3 = (w1 * x2).sum(-1)
        b = self.fc(x2).mean(-1)

        return w3 + b


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(1, 4, 64, 64)
