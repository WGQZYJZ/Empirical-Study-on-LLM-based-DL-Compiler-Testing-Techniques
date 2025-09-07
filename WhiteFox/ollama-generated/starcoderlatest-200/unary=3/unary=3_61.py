
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.rand((1, 8))
        v2 = torch.randn(1, 8)
        v3 = torch.cat([v1, v2], dim=0) # Concatenate the first dimension of v1 and v2 to the third dimension
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8)
