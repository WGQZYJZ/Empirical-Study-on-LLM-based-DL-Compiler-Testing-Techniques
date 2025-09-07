class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):
        v1  = torch.einsum('b...k,bk...->b...k',query,key) 
        v2 = v1 / math.sqrt(key.size(-1))
        v3  = v2 + attn_mask
        v4  = torch.softmax(v3, dim=-1)
        v5 = torch.einsum('...a,...a->...',value,v4) # Compute the dot product of the value tensor and the attention weights
