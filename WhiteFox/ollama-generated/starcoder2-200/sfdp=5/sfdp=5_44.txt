
class Model(torch.nn.Module):
    def __init__(self, query, key, value, attn_mask=None, dropout_p=0.5, batch_first=True):
        super().__init__()
 
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=query.size(-1), num_heads=8)
        self.dropout  = torch.nn.Dropout(dropout_p)
 
    def forward(self, query, key, value, attn_mask):
        v1  =  qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v2  = self.attn(qk + attn_mask)[0]
        v3  = torch.softmax(v2, dim=-1)
        v4  = dropout(v3, dropout_p)
 
        return value @ v4


# Initializing the model
query = torch.randn(64, 512)
key   = torch.randn(64, 512)
value = torch.randn(64, 512)
attn_mask = torch.rand(64, 300) > .9
 
m = Model(query, key, value, attn_mask=attn_mask, batch_first=True).cuda()


# Inputs to the model
__output__  = m(query, key, value, attn_mask)
