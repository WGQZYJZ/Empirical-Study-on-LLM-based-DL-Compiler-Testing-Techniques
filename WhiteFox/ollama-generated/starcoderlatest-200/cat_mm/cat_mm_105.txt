
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1 for _ in range(5)]) # Concatenation of the result tensor along the specified dimension is performed 5 times
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
