
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scale  = math.sqrt(key.shape[-1]) # Computes the square root of number of columns in a tensor. In this example it is equal to 512 
        inv_scale  = torch.as_tensor(1 / scale)
 
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2 = v1 * inv_scale
 
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5, training=True) # Apply dropout to the softmax output
        v5  = v4.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v5

# Initializing the model
m = Model()

 # Inputs to the model
 query  = torch.rand(2, 60, 128).to("cuda") 
 key = torch.rand(2, 3797, 128)
 value  = torch.rand(2, 512, 4)
__output__  = m(query, key, value)

