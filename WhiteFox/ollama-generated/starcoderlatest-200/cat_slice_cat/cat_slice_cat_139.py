
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807] # Slice the concatenated tensor along dimension 1
        return v2


# Input tensor to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 193, 193)

# Initializing the model
m = Model()
