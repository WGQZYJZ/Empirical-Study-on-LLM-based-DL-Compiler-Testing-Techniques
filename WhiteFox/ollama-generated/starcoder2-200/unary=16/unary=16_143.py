
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(384, 6)

    def forward(self, x1):
        v1  = self.fc1(x1) 
        v2 = torch.relu(v1)
        return v2

# Initializing the model
m2 = Model()


# Inputs to the model
x2  = torch.randn(384)
__output___  = m2(x2)

