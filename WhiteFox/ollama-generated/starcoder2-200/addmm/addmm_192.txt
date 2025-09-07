
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1)  # perform matrix multiplication on two input tensors
        if not isinstance(inp, torch.Tensor):
            raise TypeError('Argument is missing')
        v2 = v1 + inp
        return v2

# Initializing the model with keyword argument "inp" specified in forward
m = Model()
__output__  = m(torch.randn(5), 0)

