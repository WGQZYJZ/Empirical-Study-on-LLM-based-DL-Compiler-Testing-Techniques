
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v3 = torch.nn.functional.dropout(x1, 0.5) # Dropout with dropout probability of 0.5 applied to input tensor
        v4 = torch.rand_like(v3) 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 2)

__output__  = m(x1)

# Description of outputs
__output__: output tensor with size [N,2]

__outputs_shape__: {0: {N: 2}}

