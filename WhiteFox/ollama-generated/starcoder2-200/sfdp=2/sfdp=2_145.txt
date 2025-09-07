
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0., scale_factor=1e-6):
        v  = torch.matmul(query,  key.transpose(-2,-1)) 
        v2 = v.div_(scale_factor) # scale the dot product by an inverse scale factor
        v3  = v2.softmax(dim=-1)  # Apply softmax to the scaled dot product
        
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)   # Apply dropout to the softmax output
        v5 = v4.matmul(value)
        return v5

# Initializing the model
m  = Model()

# Inputs to the model
qk  = torch.randn(20, 1963, 1789).div_(0.01575023) # Generate an input for the query
k   = torch.randn(20, 1789, 1415).div_(0.007954734565483864) # Generate an input for the key
v    = torch.randn(20, 1963, 1415).div_(0.007954734565483864) # Generate an input for the value

 