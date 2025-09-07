
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask): 
        v1 = torch.einsum('...ij,...jk->...ik',  # Compute the dot product of the query and key
                         query,  
                     key.transpose(-2,-1) / math.sqrt(query.size(-1)))
        v2 = v1 + attn_mask
        
        v3 = torch.softmax(v2, dim=-1) 
        v4 = torch.einsum('...ij,...jk->...ik',  # Compute the dot product of the attention weights and the value
                         v3, 
                       value)
        return v4

# Initializing the model
m = Model()


# Inputs to the model
query_tensor = torch.randn(128, 500, 768).normal_(std=0.1) # query tensor of size [batch size x seq length x embedding dimension] 
key_tensor = torch.randn(128, 768, 500).normal_(std=0.1)   # key tensor of size [batch size x embedding dimension x seq length]
value_tensor = torch.randn(128, 30409, 500).normal_(std=0.1)  # value tensor of size [batch size x seq length x embedding dimension]


attn_mask  = torch.ones(query_tensor.size(), device="cuda")

# Running the model with the inputs above.
m(query_tensor, key_tensor, value_tensor, attn_mask)
