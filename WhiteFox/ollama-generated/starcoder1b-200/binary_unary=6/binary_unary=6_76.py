
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)
 
    def forward(self, x):
        v = self.linear(x) - 5
        return relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 20)
