
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x, other):
        v1 = self.linear(x) + other
        return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10)
other = torch.randn(1, 5)
