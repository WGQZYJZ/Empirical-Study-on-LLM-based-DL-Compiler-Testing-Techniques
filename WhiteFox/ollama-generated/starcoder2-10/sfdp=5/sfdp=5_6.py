
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(dim)
 
    def forward(self, query=None, key=None, value=None, mask=None):
        o, attn_w  = self.att(query, key, value, mask)
        return o


# Initializing the model
m = Model(32)

 # Inputs to the model
q1  = torch.randn(56,  8000).to("cuda")
k1  = q1 + torch.randn_like(q1) * 4
v1  = k1 + torch.randn_like(k1) / 2
 
__output__  = m(query=q1, key=k1, value=v1).to("cuda")

