
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other_scalar
#        print(other_scalar.__dict__)
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(64, 64 * 3).view(-1, 64* 64 * 3) # reshape 1 3D tensor into 5072D vector (1 96 96)
 
# Output of the model for a new input `x1`
