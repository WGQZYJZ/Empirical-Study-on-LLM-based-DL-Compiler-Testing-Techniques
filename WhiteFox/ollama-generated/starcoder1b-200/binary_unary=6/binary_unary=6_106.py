
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
 
    def forward(self, x):
        v1 = self.linear(x) - 1
        return torch.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10)
