
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v3 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 3)
x2 = torch.randn(4, 5, 6)
