
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk  = torch.einsum('...jd, ...kd -> ...jk',query,key) # Compute the dot product of the query and key tensors
        d_k = query.size(-1)
        qk  = qk / math.sqrt(d_k)
        
        if attn_mask is not None:
            qk += attn_mask.bool()
        attn_weight  = torch.softmax(qk, dim=-1) # Compute the softmax of the dot product of the query and key tensors
 

        output = torch.einsum('...jk,...jd -> ...kd',attn_weight,value) # Compute the weighted sum of the value tensor using the attention weights
        return output

# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
query = torch.randn(1024, 64)
key = torch.randn(1024, 64)
value = torch.randn(1024, 32768)
attn_mask= None

 # Initializing the mask tensor
attn_mask  = torch.ones(query.size())

 