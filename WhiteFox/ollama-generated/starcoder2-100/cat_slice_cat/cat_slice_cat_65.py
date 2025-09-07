
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): 
        v1 = torch.cat([x1, x2], dim=1) # Concatenate input tensors along dimension 1
        v2 = v1[:, :9223372036854775807] # Slice the concatenated tensor along dimension 1
        v3 = v2[:, :] # Sliced tensor along dimension 1, should not raise errors.
        return v3
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(50, 94)
x2 = torch.randn(50, 8)
__output__  = m(x1, x2)

