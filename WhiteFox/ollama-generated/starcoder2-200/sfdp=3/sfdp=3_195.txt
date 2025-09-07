
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key) # Compute the dot product of the query and key tensors
        v2  = v1.mul(scale_factor) # Scale the dot product by a factor
        v3  = v2.softmax(-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(16, 70928)
key    = torch.randn(16, 70928)
value  = torch.randn(3, 512, 49, 49)
 
__output__  = m(query, key, value)

