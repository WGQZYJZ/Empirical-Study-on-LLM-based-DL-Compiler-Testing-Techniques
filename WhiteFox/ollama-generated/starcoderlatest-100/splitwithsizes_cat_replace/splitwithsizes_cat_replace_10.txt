
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 8, dim=1) # Split along the channel dimension using tensor splitting operator
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=1) # Concatenate along the channel dimension
        return v2


# Inputs to the model
x1 = torch.randn(3, 64, 64)
