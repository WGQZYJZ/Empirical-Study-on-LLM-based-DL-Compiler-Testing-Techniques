
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        attn_mask = torch.zeros([q1.size(-2), 0, q1.size(-2), q1.size(-3)]).to(q1)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_weight = torch.softmax(qk + attn_mask, dim=-1)
        output = attn_weight @ value
        return output
 
 # Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(1, 8, 64, 64)
k1 = torch.randn(1, 8, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
