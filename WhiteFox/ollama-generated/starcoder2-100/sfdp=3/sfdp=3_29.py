
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v2  = v1 / math.sqrt(v1.size(-1))                # Scale the dot product by a factor
        v3  = v2 * 0.7946                                     # Apply pointwise convolution to the output of the dot product
        v4  = torch.softmax(v3, dim=-1)                     # Apply softmax to the scaled dot product
        v5  = v4 / math.sqrt(dropout_p)                       # Divide by a factor 
        v6  = v2 * 0.7946                                     # Apply pointwise convolution to the output of the dot product
        v7  = torch.nn.functional.softmax(v3, dim=-1)          # Apply softmax to the scaled dot product
        v8  = v7 / math.sqrt(dropout_p)                       # Divide by a factor 
        return v6
 
 
m2  = Model()
 
# Initializing the model
m2(torch.randn(3, 4), torch.randn(5, 4))
 
# Input tensors to the model
x1  = torch.randn(80, 768) # Query tensor
x2  = torch.randn(80, 768) # Key tensor
x3  = torch.randn(80, 768) # Value tensor
 
x4__output__  = m2(x1, x2, x3)

## Model
# Initializing the model
m2 = Model()

## Input tensors to the model
x5 = torch.randn(1, 507986, 768) # Query tensor
x4