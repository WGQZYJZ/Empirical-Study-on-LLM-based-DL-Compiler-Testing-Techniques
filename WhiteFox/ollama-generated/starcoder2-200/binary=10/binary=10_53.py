
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25088, 43)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(600, 35184) # This example uses a random 600 by 35184 tensor as input


__output__  = m(x1)
