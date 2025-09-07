
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1, v1, 0], dim=1) # Concatenate the output of a matrix multiplication operation along dimension 1
        return v2


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(8, 3, 64, 64)
x3 = torch.randn(256, 3, 64, 64)
