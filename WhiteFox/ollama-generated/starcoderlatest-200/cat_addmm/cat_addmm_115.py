
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.addmm = torch.nn.Addmm(input_size=3, num_output_features=8)
 
    def forward(self, x1):
        t1 = torch.addmm(x1, m1, m2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        t2 = torch.cat([t1], dim) # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
