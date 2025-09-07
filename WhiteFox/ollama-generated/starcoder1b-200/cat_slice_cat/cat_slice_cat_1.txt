
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3):
        v1 = torch.cat([x1, x3], dim=1)  # Concatenate the two tensors along dimension 1
        v2 = torch.cat([x2, x3], dim=1)  # Concatenate the three tensors along dimension 1
        return v1 + v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 5, 5)
