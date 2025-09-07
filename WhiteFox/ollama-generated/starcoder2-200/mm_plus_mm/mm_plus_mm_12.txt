
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, x2, y2, z2):
        v0  = torch.mm(x1,y1) 
        v1  = torch.mm(z1,z2) 
        return v0 + v1

# Initializing the model and initializing the inputs to the model. 
m  = Model() # Initialized with random values
x1  = torch.randn(456379, 8192).requires_grad_(True)
y1  = torch.randn(8192, 4096).requires_grad_(True)
z1  = torch.randn(4096, 1).requires_grad_(True)
x2  = torch.randn(37503, 4096).requires_grad_(True)
y2  = torch.randn(4096, 8192).requires_grad_(True)
z2  = torch.randn(8192, 1).requires_grad_(True)

 # Run the forward pass and get the output of the model as an intermediate value for the backward pass to be executed on.
__output__  = m(x1, y1, z1, x2, y2, z2)
