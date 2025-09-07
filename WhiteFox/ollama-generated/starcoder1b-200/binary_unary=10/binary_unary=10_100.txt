
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)
 
    def forward(self, x):
        v = self.linear(x) + other
        return relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(4, 1, 3, 3)
