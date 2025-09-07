
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(10, 8)
 
    def forward(self, x2):
        v1 = self.query(x2) # Apply linear transformation to the input tensor
        v2  = torch.einsum("ab,bc->ac", (v1, torch.ones_like(v1))) # Compute the dot product of the matrix multiplication of two matrices 
        v3  = torch.div(v2, 0.7) # Scale by a constant value
        return v3
# Initializing the model