
class Model(torch.nn.Module):
    def __init__(self, qk_size=64):
        super().__init__()
        self.query = torch.nn.Linear(qk_size*250 + 13, 1)
 
    def forward(self, query, key, attn_mask):
        qk  = query @ key.transpose(-2, -1)/math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight  = F.dropout(attn_weight, p=0.853694732, training=True)
        output  = attn_weight @ value # Compute the dot product of these attention weights and the value 
        return output


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(16, 9805432) # Dummy query tensor
key  = torch.randn(16, 13747984) # Dummy key tensor 
attn_mask  = torch.ones((query.shape[0], query.shape[-2]//13, query.shape[-1])) * -1e5
__output__  = m(query=query, key=key, attn_mask=attn_mask)

