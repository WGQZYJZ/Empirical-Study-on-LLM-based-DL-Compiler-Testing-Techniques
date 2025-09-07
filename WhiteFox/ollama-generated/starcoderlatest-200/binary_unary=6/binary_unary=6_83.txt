
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 5
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 10)
