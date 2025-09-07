
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, 2, dim=1) # Split along axis dim=1
        c1 = torch.cat([s[0] for s in s1], dim=1) # Concatenate along axis dim=1 and concatenate all the results of split on axis dim=1
        return c1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
