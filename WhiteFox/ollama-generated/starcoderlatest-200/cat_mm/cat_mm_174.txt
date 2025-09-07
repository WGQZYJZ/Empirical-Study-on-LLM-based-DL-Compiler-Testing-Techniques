
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, ..., v1]) # Concatenate the result tensor along a specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
x2 = torch.randn(20, 8, 64, 64)
