
class SelfAttentionBlock(torch.nn.Module):
    def __init__(self, dmodel=320, nhead=4, dropout=0.1, bias=True):
        super().__init__()

        self.dropout = torch.nn.Dropout(p=dropout)
        
        self.norm1  = torch.nn.LayerNorm([dmodel])
        self.norm2  = torch.nn.LayerNorm([dmodel])
 
        self.attn  = torch.nn.MultiheadAttention(d_model=dmodel, num_heads=nhead)
    
    def forward(self, query, key, value):
        v1  = self.norm1(query) @ self.norm2(key)
        v2  = v1.transpose(-2, -1) / math.sqrt(v1.size(-1))
        v3  = v2 + attn_mask
        v4  = torch.softmax(v3, dim=-1)
        v5  = self.dropout(v4) @ value
        return v5


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.attnblock = SelfAttentionBlock()

    def forward(self, q, k, v):
        v1  = self.attnblock(q, k, v)
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
__query_input__  = torch.randn([320]) # random vector of length 320 that represents query
__key_input__  = torch.randn(5, [768] + 40)
__value_input__  = torch.randn(40,)


# Initializing the model - 1 
m  = Model()


# Inputs to the model - 1
q  = torch.randn([320]) # random vector of length 320 that represents query in the first execution 
k  = torch.randn(5, [768] + 40)
v  = torch.randn(40,)

