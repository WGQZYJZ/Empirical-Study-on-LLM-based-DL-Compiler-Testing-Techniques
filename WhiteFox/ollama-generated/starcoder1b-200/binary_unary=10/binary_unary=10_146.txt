
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64, 1)
 
    def forward(self, x1):
        v1 = torch.reshape(x1, -1, 64 * 64)
        v2 = torch.relu(v1)
        v3 = self.linear(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 64)
