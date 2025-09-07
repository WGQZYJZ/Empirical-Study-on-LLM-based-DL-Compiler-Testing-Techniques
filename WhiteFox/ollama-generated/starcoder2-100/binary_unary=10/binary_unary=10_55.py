
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0):
        v  = self._init_weights()
        v1 = torch.nn.functional.linear(v, 1) # Applying the linear transformation to the input tensor
        v2 = v1 + other # Add another constant tensor of the same size to the output of the linear transformation

        return v2

class _Submodel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._linear  = torch.nn.Linear(3, 8)
        self._relu    = torch.nn.ReLU()

    def forward(self, x1):
        return self._relu(self._linear(x1))

# Initializing the model
m_1 = Model().eval() # Using eval mode for avoiding gradient calculation in the backward pass

def m_2(x1):
    return _Submodel()(x1)

# Inputs to the model
x1  = torch.randn(3, 8)
