
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3, 2)
        self.fc2 = torch.nn.Linear(3, 5)
 
    def forward(self, x):
        v1 = self.fc1(x)
        v2 = v1 + 1
        v3 = self.fc2(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 64)
