
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
 
        # Initializing the matrix 1 as a constant with dimensions of (32, 64) and another matrix 2 similarly for a tensor 3
        self.mat1 = torch.tensor(np.zeros((32, 64)), requires_grad=True) 
        self.mat2 = torch.tensor(np.zeros((32, 64)), requires_grad=True)
        self.tensor3 = torch.randn(1024, 32, 64).requires_grad_(True)
 
        # Initializing the linear layer with bias
        self.linear = torch.nn.Linear(32*64 + 32*64+32*64, 80)
 
    def forward(self):
        
        v1 = torch.addmm(self.tensor3, self.mat1, self.mat2) # Performing a matrix multiplication of the input tensor and two matrices
        v2 = torch.cat([v1], dim=0).sum() # Concatenate along a specified dimension which is 0 here. This concatenates the matrix product result along dimension number zero. The output from this operation is summed up to obtain a single tensor.

        return self.linear(v2)


# Initializing the model, setting the batch size for each tensor as 16 and passing a random tensor with shape of (3, 4).
dim = 0 # Setting dimension number zero
m  = Model(dim=0) 
torch.set_grad_enabled(True)


# Inputs to the model
x1 = torch.randn(57280, 96).requires_grad_(True) # The input tensor of shape (3, 4) with size 3 and 4 along dimension number zero respectively
__output__  = m()

