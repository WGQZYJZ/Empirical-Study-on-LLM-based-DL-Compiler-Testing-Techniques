
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*32, 100)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32*32))
        v2 = v1 - 1
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 3, 64, 64)
