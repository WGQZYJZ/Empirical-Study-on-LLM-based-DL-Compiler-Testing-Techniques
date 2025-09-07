
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4096*128+3, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other # The `other` tensor is passed as a keyword argument here
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()
 
# Inputs to the model
other = torch.randn(4096*128+3, 5) # This is an optional input that will be passed as a keyword argument when calling `forward`. In the example below this input has size `[768 + 3]`, which doesn't match the size of the `other` tensor above.
x1 = torch.randn(4096, 5)
 
__output__  = m(x1, other=other).sum()
