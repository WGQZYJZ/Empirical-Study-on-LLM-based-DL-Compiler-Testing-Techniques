
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        if not isinstance(x1, torch.Tensor) or not isinstance(inp, torch.Tensor):
            raise ValueError('Please provide 2 tensors')
 
        v1 = torch.mm(x1, x1)
        v2 = v1 + inp
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(5,4)
inp = torch.rand(5, 4) # It can be any tensor of the appropriate size, like zeros or ones.
