
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk = torch.matmul(query, key) / math.sqrt(query.size(-1))
 
        if not attn_mask is None:
            qk  = qk + attn_mask
 
        qk = nn.Softmax(qk, dim=-1) 
        output = torch.matmul(qk, value)
        return output
 
model = ScaledDotProductAttention()


# Initializing the model
m = model()


# Inputs to the model
query  = torch.randn(4, 320 ,8 )
key    = torch.randn(4, 176 ,8)
value  = torch.randn(4, 175 ,8)
__output__= m(query, key, value)

