
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Compute the product
        v2 = torch.cat([v1, v1, ..., v1], dim=-1)  # Concatenate the result of the product along the last dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 8, 64, 64)
