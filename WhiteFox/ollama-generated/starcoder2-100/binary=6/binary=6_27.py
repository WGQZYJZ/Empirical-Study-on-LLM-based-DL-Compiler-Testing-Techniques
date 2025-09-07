
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v3 = v1 - other_tensor
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(10, 2)
other_tensor  = torch.randn(1, 5).long() # For illustration purpose, this line is omitted in the actual example

__output__  = m(x1)
