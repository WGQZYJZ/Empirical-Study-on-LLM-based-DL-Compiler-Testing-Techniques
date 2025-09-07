
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(3072, 5)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, mat1, mat2) # Add the matrix multiplication of a first and second set of matrices to an input tensor
        v2 = torch.cat([v1], dim) # Concatenate along a specified dimension
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3072, 64) # The shape of x1 should be different from x1_0 and x1_1 in this scenario. It's required that they don't overlap in any dimension (except possibly the batch axis) with respect to all other tensor dimensions.
x2 = torch.randn(5, 64) # The shape of x2 should match x1
