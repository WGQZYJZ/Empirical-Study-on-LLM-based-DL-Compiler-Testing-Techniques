
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(100, 32)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = torch.nn.ReLU()(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5000, 32)
