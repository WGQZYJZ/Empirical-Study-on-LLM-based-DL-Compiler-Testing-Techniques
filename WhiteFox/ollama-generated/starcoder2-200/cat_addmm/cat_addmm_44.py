
class Model(torch.nn.Module):
    def __init__(self, dim1=2048, dim2=512, mat_rows=3, mat_cols=5):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(dim1, 768)
        self.linear2 = torch.nn.Linear(mat_rows * mat_cols + 768 , dim2)
 
    def forward(self, x):
       v0   = torch.addmm(x, self.linear1.weight, self.linear1.bias) # Performs a matrix multiplication and adds it to the input tensor
       v1   = F.relu(v0 + 3.14)# Add bias to the output of the first linear layer
       v2   = torch.addmm(v1, 6.789, self.linear2.weight) # Multiply a matrix by another matrix and add it to the input tensor
       v5_t = F.relu(torch.cat([v2], dim=1))# Concatenate along the specified dimension

# Initializing the model
m = Model()
 
# Inputs to the model
x  = torch.randn(4, 3)
__output__  = m(x)

