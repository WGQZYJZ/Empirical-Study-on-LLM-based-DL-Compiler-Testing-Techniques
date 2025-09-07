
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.addmm(input_tensor, mat1, mat2)  # Perform a matrix multiplication of the result from a previous operation and mat2 and add it to the input tensor
        v2 = torch.cat([v1], dim=0) # Concatenate the result along the specified dimension
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
