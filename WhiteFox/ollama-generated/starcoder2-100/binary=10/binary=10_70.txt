
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 5) # A matrix of dimension (4, 5), each entry is a normally distributed random number with mean zero and standard deviation one.
x2 = torch.randn(3, 5) # A matrix of dimension (3, 5), each entry is a normally distributed random number with mean zero and standard deviation one.

 __output__1m(x1, x2)

 