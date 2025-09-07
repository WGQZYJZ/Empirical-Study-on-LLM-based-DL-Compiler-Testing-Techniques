
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1000, 50)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = F.relu(v1)

# Initializing the model
m2 = Model()

 # Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output2__ = m2(x2)

