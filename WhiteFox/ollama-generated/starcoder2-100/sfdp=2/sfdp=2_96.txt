
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v1  = torch.matmul(query1, key2.transpose(-2, -1)) # Compute the dot product of the query and the key
        v2 = v1 / 768e-05  # Scale the dot product by the inverse scale factor
        v3  = v2.softmax(dim=-1) 
        v4 = torch.nn.functional.dropout(v3, p=0.25)  
        v5  = v4.matmul(value3)
        return v5


# Initializing the model
m  = Model()
 
# Inputs to the model
q = torch.randn(64, 768) # A random query vector of size (768,) for the query in a Transformer model
k1 = torch.randn(32, 30544) # A random key vector of size (30544,), which is used as input to the first layer of self-attention modules
v2  = torch.randn(64, 768)  # A random value vector of size (768,) for the value in a Transformer model
 

# __output__ is a randomly generated pytorch tensor variable

