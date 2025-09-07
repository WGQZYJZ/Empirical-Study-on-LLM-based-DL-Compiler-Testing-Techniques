
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dim=1):
        v1 = torch.addmm(x1, m1, m2) # Add the first input and second input tensor along dimension "dim"
        v2 = torch.cat([v1], dim) 
        return v2
 

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
