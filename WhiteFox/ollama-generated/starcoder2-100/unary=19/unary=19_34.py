

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(4, 2)
 
    def forward(self, x1):
        v0 = x1[:, -2] # Get the last element of each row in a 3D tensor of size (N, 64, 3). If x is Nx64x3, the output will be a 3D tensor of size (N, 1)
        v1  = self.lin(v0) # Apply the linear transformation to this last element
        v2 = torch.sigmoid(v1) # Apply sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 64*3) 

# Adding the last dimension for the input tensor based on user specification 
new_tensor = torch.zeros([x1.shape[0], x1.shape[-1]+1])
for i in range (len(new_tensor)):
  new_tensor[i][:-2] = x1 [i].T
  
__output__  = m(torch.unsqueeze(new_tensor, -1))