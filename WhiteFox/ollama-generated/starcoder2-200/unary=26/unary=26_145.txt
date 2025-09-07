
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v0 = torch.randperm(23) # Generate random permutation of integers between 0 and 23.
       v1 = torch.rand(4, 5, dtype=torch.int64) # Generate a tensor of integer values with size (4, 5).
       v2 = x1[:, [v0[i] for i in range(x1.size(-1))], :] # Retrieve elements from the last dimension of input `x1`. 
       v3 = torch.unique_consecutive(v1) # Find unique values and their counts in tensor `v1`
       v4  = self.conv2d(v0) # Apply pointwise convolution to tensor `v0`
       return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 8, 56, 56)
__output__  = m(x1)


