
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()
other = 3.5

# Inputs to the model
x  = torch.randn(4,784) # a 2D matrix representing the input of the model 
