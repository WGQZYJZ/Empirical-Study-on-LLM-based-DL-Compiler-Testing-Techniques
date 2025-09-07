
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value): 
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of a query and a key
        v2  = v1.div(torch.nn.functional.hardswish(v1.shape[-1]).view(-1))  # Scale the dot product by a hardswish activation function
        v3  = torch.nn.functional.softmax(v2, dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.5, training=self.training)  # Apply dropout to the softmax output
        v5  = value * torch.nn.functional.gelu_new(v4) # Compute the dot product of a dropout output and a value
        return v5


# Initializing the model
m  = Model()

# Inputs to the model
query, key, value  = (torch.randn(1,32,8), torch.randn(1,32,8), torch.randn(1,32,8))

__output__  = m(query,key,value)
