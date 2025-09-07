
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.dim  = dim

    def forward(self, x1):
        mat1 = torch.randn(256)
        mat2 = torch.randn(256)

        v1  = torch.addmm(x1, mat1, mat2)
        v2  = torch.cat([v1], self.dim)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(64) # Initialize an input tensor with a specified shape of [batch_size, num_features]

# Output from the model
out  = m(x1)

# Saving the output as a reference for subsequent inputs validation
__output__  = out

