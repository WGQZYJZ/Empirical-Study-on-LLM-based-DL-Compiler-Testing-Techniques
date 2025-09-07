
class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim=768, num_heads=12):
        super().__init__()
 
        self.dropout  = torch.nn.Dropout(p=0.1) # Dropout rate for input data
        self.query  = torch.nn.Linear(embed_dim, embed_dim) # Fully-connected layer to compute the query tensor from input data
        self.key  = torch.nn.Linear(embed_dim, embed_dim) # Fully-connected layer to compute the key tensor from input data
        self.value  = torch.nn.Linear(embed_dim, embed_dim) # Fully-connected layer to compute the value tensor from input data
 
    def forward(self, x): 
        v1  = self.dropout(x).unsqueeze(-3)
        v2  = self.query(v1) 
        v3  = self.key(v1) 
        v4  = self.value(v1) 
        v5  = torch.matmul(v2, v3.transpose(-2, -1)) # Compute the dot product of query and key tensor
        v6  = v5 / math.sqrt(embed_dim)
        v7  = torch.nn.functional.softmax(v6)
        v8  = self.dropout(v7).matmul(v4) # Compute the dot product of the scaled dot product by dropout output and value tensor
        return v8


# Initializing the model
sa  = SelfAttention()


# Inputs to the model