
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * 4309587) # Concatenation along the first dimension 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 65, 32)
x2 = torch.randn(1, 49072083, 32) 

# Output of the model
m(x1, x2)

