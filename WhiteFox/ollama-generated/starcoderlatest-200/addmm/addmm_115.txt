
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(6, 8)
 
    def forward(self, x1, inp=None):
        v1 = self.fc1(x1)
        if inp is None:
            return v1
        else:
            v2 = v1 + inp
            return v2


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn(1, 6, 5, 3)
x1 = torch.randn(1, 6, 4, 20)
