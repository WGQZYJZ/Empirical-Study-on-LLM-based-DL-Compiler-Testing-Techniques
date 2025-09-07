
class Model(torch.nn.Module):
    def __init__(self, input1, input2, *args):
        super().__init__()

    def forward(self, x1):
        v1  = torch.cat([x1] + args) # Concatenate tensors with more than one element along a specified dimension
        v2 = torch.nn.functional.tanh(v1) # Apply a pointwise unary operation to the reshaped tensor.
        return v2

# Initializing the model 
m  = Model(x, y, z)
__output__  = m()

