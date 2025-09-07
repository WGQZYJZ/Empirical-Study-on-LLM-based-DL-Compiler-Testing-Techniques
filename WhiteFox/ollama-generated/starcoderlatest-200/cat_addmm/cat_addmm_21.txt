
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.mat = torch.eye(8, 2)

    def forward(self, x1):
        t1 = torch.addmm(x1, self.mat[0], self.mat[1]) # Add a matrix multiplication between mat and the input tensor along dimension dim
        t2 = torch.cat([t1], dim=dim) # Concatenate the result along a specified dimension
        return v6


# Initializing the model
m = Model(dim=2)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
