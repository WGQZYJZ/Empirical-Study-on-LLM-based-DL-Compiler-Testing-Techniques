
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1 + other


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(1, 100)
