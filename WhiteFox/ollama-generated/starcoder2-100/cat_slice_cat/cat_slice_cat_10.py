
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v = torch.cat([x[0], x[-2]], dim=1)
        return v[:9223372036854775807][:size]


# Initializing the model
m  = Model()
 
# Inputs to the model
x  = [torch.randn(2, 3), torch.randn(1)] + ([0]*9) # The length of x is dynamic. And all elements in x are tensors with the same size.
__output__  = m(x)

