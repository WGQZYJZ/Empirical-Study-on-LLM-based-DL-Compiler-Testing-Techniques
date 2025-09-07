
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        other = torch.randn(5, 10)
        return v3 + other


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 1024)
