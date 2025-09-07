
class Model(torch.nn.Module):
    def __init__(self, hidden_size=64):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(hidden_size, hidden_size, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = (v2 * v4).div_(1 + torch.exp(-v2))
        v6 = v5.matmul(x2)
        return v6


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(1, 3, 8, 8)
k1 = torch.randn(1, hidden_size, 1, 1)
v1 = torch.randn(1, hidden_size, 1, 1)
