
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, v1 + 3) / 6 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5) # The size of this input is determined by the number of nodes in the model that feeds into the output of the linear transformation
__output__  = m(x1)

