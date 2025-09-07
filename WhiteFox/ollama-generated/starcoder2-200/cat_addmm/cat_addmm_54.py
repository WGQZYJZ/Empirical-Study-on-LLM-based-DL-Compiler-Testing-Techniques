
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.addmm(x1, x2) # Apply a matrix multiplication of the input tensors and a 5x4 matrix
        v2  = torch.cat([v1], dim=0) 
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(3, 64) # A 3-dimensional tensor of shape [batch size (3), sequence length (64)]
x2  = torch.rand(5, 4)   # A 2-dimensional tensor of shape [5, 4]

 