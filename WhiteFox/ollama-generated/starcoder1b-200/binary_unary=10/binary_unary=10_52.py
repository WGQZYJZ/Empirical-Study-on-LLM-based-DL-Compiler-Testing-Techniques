
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1) + x1
        return torch.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
