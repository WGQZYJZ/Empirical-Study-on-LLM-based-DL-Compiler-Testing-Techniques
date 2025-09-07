
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.dim  = dim
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 + self.dim * v1  # Add another dimension in each input tensor
        v3 = v2 + self.dim * v2  # Add another dimension in the matrix multiplication result of the concatenation operation
        return v3


# Initializing the model
m = Model()


