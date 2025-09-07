
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.relu(x1[:, :3] + 1) # Linear transformation on the 2-dimension input tensor.
        v2  = self._linear_transform(v1) 
        return v2 

    def _linear_transform(self, t):
        return torch.nn.functional.linear(t, ...)


# Initializing the model
m  = Model()
# Inputs to the model
x1  = torch.randn(30, 5) # Input of the model. 
__output__  = m(x1)