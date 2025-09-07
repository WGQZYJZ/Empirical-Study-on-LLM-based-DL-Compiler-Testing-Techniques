
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(2, 3)
 
    def forward(self, x1, x2):
        v1 = self.fc(x1)
        return self.fc(torch.cat([v1, v1, ...], dim=1))


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 2, requires_grad=True)
x2 = torch.randn(3, 3, requires_grad=True)
