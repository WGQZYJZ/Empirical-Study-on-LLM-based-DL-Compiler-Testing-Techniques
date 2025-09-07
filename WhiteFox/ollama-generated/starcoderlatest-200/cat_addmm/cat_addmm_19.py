
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, m1, m2)
        v2 = torch.cat([v1], dim=0) # Concatenate the result along the specified dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
x2 = torch.randn(8, 6, 64, 64)
