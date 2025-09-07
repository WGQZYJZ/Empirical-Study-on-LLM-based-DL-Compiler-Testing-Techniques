
class Model(torch.nn.Module):
    def __init__(self, mat_shape=(128,), dim=0):
        super().__init__()
        self.t1 = torch.randn(*mat_shape)
        self.t2 = torch.randn(*mat_shape)
 
    def forward(self, input):
        t1 = torch.addmm(input, self.t1, self.t2)  # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim)  # Concatenate the result along a specified dimension
        return t2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
