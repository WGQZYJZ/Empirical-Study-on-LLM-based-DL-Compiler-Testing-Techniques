
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 256)
        self.linear1= torch.nn.Linear(256,8*8*384)
 
    def forward(self, x1):
        v1  = linear_(x1) # Apply a linear transformation to the input tensor
        v2  = v1  - 'other' # Subtract 'other' from the output of the linear transformation
        v3  = torch.relu(v2)# Apply the ReLU activation function to the result
        return v3


# Initializing model
m = Model()
x1  = torch.randn(8, 4096)

__output__  = m(x1)