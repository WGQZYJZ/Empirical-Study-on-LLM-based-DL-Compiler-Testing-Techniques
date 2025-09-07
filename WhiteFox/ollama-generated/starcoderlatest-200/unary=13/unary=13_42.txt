
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(128 * 544 * 3, 64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = sigmoid(v1)
        v3 = v1 * v2
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
