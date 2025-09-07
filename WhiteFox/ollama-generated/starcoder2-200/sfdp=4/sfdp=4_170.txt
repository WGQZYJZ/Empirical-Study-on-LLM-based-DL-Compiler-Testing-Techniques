
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk  = torch.einsum('...i..., ...j->...ij', [query, key]) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensor
        if attn_mask is not None:
            qk += attn_mask
 
        attn_weight  = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()

 # Inputs to the model