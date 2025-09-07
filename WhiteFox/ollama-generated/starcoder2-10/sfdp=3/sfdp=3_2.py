
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, s=1., p=0.):
        o = torch.matmul(q, k.transpose(-2, -1)) * s # Compute the dot product of the query and key tensors.
        o  = torch.nn.functional.dropout(o, p) # Apply dropout to the scaled dot product.
        return o @ v
 
# Initialize model
m = Model()
 
# Inputs for the model
q  = torch.randn(20, 16, 32, 8)
k  = torch.randn(20, 16, 32, 8)
v  = torch.randn(20, 16, 32, 8)
 
__output__  = m(q, k, v)
