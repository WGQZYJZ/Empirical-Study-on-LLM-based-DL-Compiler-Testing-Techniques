
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x):
        v = self.linear(x) - 0.5 # subtract 0.5 from the output of the linear transformation
        return relu(v)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 32)
