
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(4, 5)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, x2, x3)
        v2 = self.fc(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 5)
