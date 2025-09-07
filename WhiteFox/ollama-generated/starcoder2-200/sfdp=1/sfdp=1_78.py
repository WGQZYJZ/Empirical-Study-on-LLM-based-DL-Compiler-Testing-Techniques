
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        m  = torch.matmul(q, k.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v1  = m / (m.shape[-1] ** (-0.5))       # Scale the dot product by the inverse scale factor
 
        smask  = torch.nn.functional.dropout(v1.softmax(dim=-1), p=dropout_p)
        v2  = smask * v                         # Compute the dot product of the softmax output and the value tensor
        return v2
 
# Initializing the model
m = Model()
 
 
# Inputs to the model
q = torch.randn(4, 30, 10)
k = torch.randn(4, 10, 768)
v  = torch.randn(4, 768, 256)
 
# Output of the model
__output__  = m(q, k, v)
 
 
 
