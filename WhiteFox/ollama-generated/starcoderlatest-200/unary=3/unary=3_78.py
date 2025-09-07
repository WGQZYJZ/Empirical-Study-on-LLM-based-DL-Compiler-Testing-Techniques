
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv1(x1) * 0.5
        v2 = self.conv2(v1) * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        v4 = v3 * v2
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
