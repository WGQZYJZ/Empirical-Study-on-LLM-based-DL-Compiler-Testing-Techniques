
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4, 1)
 
    def forward(self, x2): 
        v0 = torch.cat([x2, x3], dim=1) # Concatenate two tensors vertically (column-wise).
        v7  = self.linear(v0)
        return v7


# Initializing the model
m = Model()

# Inputs to the model
__output__  = m(__input__)
