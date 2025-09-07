

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.M
    ﬁ.mm = 1
        self.mm = 2

    def forward(self, x0):
        v1  = torch.mm(x0)  # matrix multiplication of two input tensors.
        v2 = torch.cat([v1] * 5)  # concatenation along a specified dimension 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4, 8, 39, 39)


# Initializing the model with the previous one
m_p = Model()
x0 = m_p._modules['mm'].weight
m.__setattr__('mm', nn.Parameter(x0))

 # Inputs to the model with the previous one
x1 = torch.randn(4, 8)

 __output__  = m(x1)

__output2__ = m(x1)

# Check whether the two outputs are identical. If not, re-generate.
assert (
    torch.allclose(__output__, __output__) or 
    torch.all((__output2__ - __output__).abs() < 0.0001))