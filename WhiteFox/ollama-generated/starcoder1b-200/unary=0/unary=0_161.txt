
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.elu(x1, inplace=True)
        v2 = F.elu(v1 * 0.5, inplace=True)
        v3 = F.square(v2) + 1
        v4 = F.elu(v3 * 0.7071067811865476)
        v5 = torch.tanh(v4) + 1
        v6 = F.elu(v1 * v5)
        return v6

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
