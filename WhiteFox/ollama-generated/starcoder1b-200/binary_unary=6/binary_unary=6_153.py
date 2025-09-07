
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)
 
    def forward(self, x):
        v = self.linear(x) - 3.5
        return relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 10)
