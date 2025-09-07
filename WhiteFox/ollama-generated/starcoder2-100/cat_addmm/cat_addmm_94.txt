
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.cat  = torch.nn.functional.concat
        self.addmm = torch.nn.functional.addmm
 
    def forward(self, input1, mat1, mat2, dim=0):
        v1  = addmm(input1, mat1, mat2) 
        v3  = cat([v1], dim)
        return v3


# Initializing the model
m = Model()
 
 # Input tensors for the model (make sure to generate input tensors of different shapes from different initializations of the model)
mat_1  = torch.randn(20, 5)
mat_2  = torch.randn(5, 64)
input1 = torch.randn(30000, 5)
 
 # Passing the input tensors to the model and getting the output tensor from the model
__output__  = m(input1, mat1, mat2)
