
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1, mat1, mat2):
        v0 = torch.Size([32]) # Size of a vector. The number 32 is just for demonstration.
        v1 = torch.zeros(*v0)
        v2 = self.conv(x1)
        v3 = torch.addmm(input=x1, mat1=mat1, mat2=mat2) # Performing a matrix multiplication and then adding the result to input tensor x1 
        v4  = torch.cat([v0], dim) # Concatenate vector v0 along dimension zero
        return v3, v4


# Initializing the model
m  = Model()
# Inputs to the model
x1 = torch.randn(256, 8 , 3, 3)
mat1 = torch.randn(4, 7 , 2 ) # A matrix with size [4, 7]
mat2 = torch.randn(7, 9) # A matrix with size [7, 9]

