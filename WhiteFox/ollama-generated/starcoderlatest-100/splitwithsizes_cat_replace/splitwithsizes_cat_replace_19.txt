
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        x2 = torch.split(x1, [4], dim=0)
        v = torch.cat([x for x in x2 if x is not None], dim=0)  # Note that None can be used to represent an empty tensor
        return v


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
