
class Model(torch.nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.dim = dim

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=self.dim) # Concatenate x1 and x2 along the dimension of dim
        return v1


# Initializing the model
m = Model(2)  # Dim should be different from previous one

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)  # Input should be a 2-d tensor of shape (n_samples, dim) with a value between -1 and +1
x2 = torch.randn(3, 8, 64, 64)
