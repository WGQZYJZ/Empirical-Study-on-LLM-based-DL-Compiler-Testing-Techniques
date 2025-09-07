
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = x1 + x2  # Perform a matrix multiplication of x1 and x2
        v2 = torch.cat([v1], dim=0)  # Concatenate the result along dimension 0
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
