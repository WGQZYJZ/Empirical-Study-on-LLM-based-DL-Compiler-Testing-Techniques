
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        v2  = v1.div(0.3789)  # Scale the dot product by a constant 0.3789
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5)  # Apply dropout with probability of 0.5 on the softmax output
        v5  = value[None] * v4[:, :, None]  # Compute the dot product of the dropout output and a value tensor
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(32,64,50)
key    = torch.randn(32,64,50)
value  = torch.randn(32,1,50)
__output__  = m(query, key, value)

