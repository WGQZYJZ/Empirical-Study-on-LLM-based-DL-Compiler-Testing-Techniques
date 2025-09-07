
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64, 10)
 
    def forward(self, x1):
        # ... other steps
        v2 = self.fc(x2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, requires_grad=True)
x2 = x1  + 1


