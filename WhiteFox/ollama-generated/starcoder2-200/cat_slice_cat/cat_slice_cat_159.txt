
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *x1):
        v2 = torch.cat([t3 for t3 in x1], dim=1) # Concatenate the input tensors along dimension 1
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = [torch.randn(size, size),
      torch.rand((10, 9)),
      torch.rand((3))]


__output__  = m(*x1)
