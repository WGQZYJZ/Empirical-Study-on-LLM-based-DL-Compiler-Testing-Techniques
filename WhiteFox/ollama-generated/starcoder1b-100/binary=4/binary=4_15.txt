
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 8)
        self.linear2 = torch.nn.Linear(32, 8)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(v1 + other)
        return v2


# Inputs to the model
inputs = ... # The input to the model
other   = ... # Another input to the model
__output__  = m(inputs, other)


