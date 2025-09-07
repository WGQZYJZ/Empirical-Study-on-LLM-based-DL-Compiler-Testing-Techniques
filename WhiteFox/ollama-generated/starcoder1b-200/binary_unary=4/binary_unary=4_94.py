
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        v = self.linear(x)
        return v + self.linear(other)


# Initializing the model
m = Model()


# Inputs to the model
inputs  = torch.randn(2, 10, 40)  # 2 examples of input
__output__  = m(inputs)


