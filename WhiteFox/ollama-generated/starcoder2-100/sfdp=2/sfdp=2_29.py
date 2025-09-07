
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key  = torch.randn(32, 10)
        self.value  = torch.randn(512, 64)
 
    def forward(self, query):
        v1  =  torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of a query and a key
        v2  = v1 / (3e-5 ) # Scale the dot product by an inverse scale factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product 
        v4  = torch.nn.functional.dropout(v3, p=0.1) # Apply dropout to the softmax output 
        __output__   = v4 .matmul(value)
        return __output__
# Initializing the model
m  = Model()

