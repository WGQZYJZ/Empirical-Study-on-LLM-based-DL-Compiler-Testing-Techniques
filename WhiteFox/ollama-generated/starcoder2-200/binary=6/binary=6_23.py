
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 - 4.859376
        return v2


# Initializing the model
m = Model()
__output__  = m(torch.randn(10)) # The size of inputs in a forward call should be 10.


# Inputs to the model
x1 = torch.randn(5)