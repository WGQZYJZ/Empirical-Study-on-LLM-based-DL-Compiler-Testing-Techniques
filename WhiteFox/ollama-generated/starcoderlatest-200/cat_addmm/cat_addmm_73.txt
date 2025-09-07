
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(4, 8)
 
    def forward(self, x1):
        v1 = self.fc1(x1)
        t2 = torch.cat([v1], dim=0)
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(24, 3, 64, 64)
