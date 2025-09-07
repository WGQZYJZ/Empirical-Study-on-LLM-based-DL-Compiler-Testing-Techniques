
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 8)
 
    def forward(self, x1, other):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2) 
        return v3


# Initializing the model
m = Model()

# Inputs to the model (first input)
x1  = torch.randn(1, 32) # This is an example input tensor for the linear transformation.

# Inputs to the model (second input)
other = torch.randn(1,8)# This is an example of another tensor passed as a keyword argument.
__output__  = m(x1, other=other)
