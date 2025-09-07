
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        v1  = (query @ key.transpose(-2,-1)) / torch.sqrt(query.size(-1))
        v2  = v1 + attn_mask
        v3  = torch.softmax(v2, dim=-1)
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
q1  = torch.randn(5000, 64000)
k1  = torch.randn(5000, 64000)
m1  = torch.randn(32789, 64000)

 __output__  = m(q1, k1, m1)

