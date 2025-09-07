
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn((32, 48)) # A random tensor of size (32, 48)
        v1  = torch.nn.Linear(v0.shape[-1], 96)(x1)
        v2  = self._add_other(v1)
        return v2
 
    def _add_other(self, input): # The "other" tensor is defined in the forward method
        v3  = torch.randn((57)) + input
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 64)
 
# Calling the forward function of the model
__output__  = m(x1)