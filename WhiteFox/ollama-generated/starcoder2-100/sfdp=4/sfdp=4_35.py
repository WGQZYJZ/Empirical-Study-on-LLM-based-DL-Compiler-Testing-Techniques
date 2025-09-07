
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query):
        key = torch.randn(32, 512)
        value = torch.randn(32, 864)
 
        v1  =  torch.einsum("ikj,jk->iik", [query,key]) # Compute the dot product of the query and key tensors
        v1 /= math.sqrt(torch.size(v1)[-1]) # Scale it using the square root of the last dimension size
        v2  = v1 + torch.randn((32,864)) # Add a random attention mask to the scaled dot product
        v3  = torch.softmax(-v2, dim=-1) # Compute the softmax over the last dimension, which is the query-key dimension
        return value @ v3  # Compute the dot product of the value and the attention weights


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(32,512)


__output__  = m(query)