
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
 
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key
        
        if attn_mask is not None:
            qk += attn_mask  # Add the attention mask to the scaled dot product
 
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output      = attn_weight @ value  # Compute the dot product of the attention weights and the value

        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
 query = torch.randn(2, 3, 15) 
 key   = torch.randn(2, 10, 15)
 value = torch.randn(2, 4, 10)
 
# Attention mask (Optional, 5 is used here as a dummy mask for demo purposes only)
attn_mask = torch.ones(query.size()[:-1]) * 3

 # Output from the model 
 output   = m(query=query, key=key, value=value, attn_mask=attn_mask)

