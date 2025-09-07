
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x2], dim=0) # Concatenate along dimension 0
        v2 = v1[:, :9223372036854775807] # Slice along dimension 0
        v3 = v2[:, :size] # Further slice along dimension 0
        v4 = torch.cat([v1, v3], dim=0) # Concatenate along dimension 0
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
x3 = torch.randn(2, 3, 64, 64)
