
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 5)
        self.fc2 = torch.nn.Linear(5, 6)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        v2 = torch.cat([v1, v1], dim=-1)
        v3 = self.fc2(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3)
x2  = torch.randn(1, 5)
