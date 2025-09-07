
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - 54.0 # The 'other' variable is a global constant here (defined in the text at the beginning of this file).
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 6)
__output__   = m(x1)

