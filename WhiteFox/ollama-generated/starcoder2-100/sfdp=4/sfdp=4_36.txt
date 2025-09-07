
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask, value):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output

# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(64,  3072).reshape(1, -1, 8, 8 )
key    = torch.randn(64, 3072).reshape(1, -1, 8 , 8)
attn_mask  = torch.ones([ query.shape[1], key.shape[1] ]).bool()
value  =  torch.randn(64, 9*9*512)

 __output__  = m(query, key, attn_mask, value)

# Generated model: