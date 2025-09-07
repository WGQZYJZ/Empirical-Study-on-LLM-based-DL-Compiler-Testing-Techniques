
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 10)

    def forward(self, x1):
        v1 = x1 * 0 + self.linear(x1)
        return v1

# Initializing the model
m2 = Model()

 # Inputs to the model
x1 = torch.randn(1, 1, 1)
