
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None): 
        v2 = self._other # Access another internal object
        v3  = v2 + 5.6 # Add a constant to the value of this object (in this case, it is 5.6)
        return torch.relu(v3), v1


# Initializing the model
m = Model()
__output__, __other_val__= m(x1)

