
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.einsum("bijc,bjd->bijd", (query,key)) 
        v2  = v1 / math.sqrt(query.size(-1)) 
        v3  = v2 + attn_mask 
        v4  = torch.softmax(v3, dim=-1)
        v5  = torch.dropout(v4, dropout_p, True)
        v6  = torch.einsum("bijd,bjd->bijd", (v5, value))
        return v6


# Initializing the model