
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x1, other=10):
        v1 = self.linear(x1) + other
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 2)
