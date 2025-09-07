
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(28, 2)
 
    def forward(self, x1):
        v1 = x1 * x1
        v2 = torch.cat([v1], dim=1)
        return self.fc(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3072)
