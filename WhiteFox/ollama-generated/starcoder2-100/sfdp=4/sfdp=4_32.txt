
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.softmax((query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)), dim=-1)
        v2  = attn_mask + v1
        v3  = v2 @ value
        return v3


# Initializing the model:
m = Model()

# Inputs to the model
q  = torch.randn(8, 64, 50).cuda()
k  = torch.randn(8, 64, 50).cuda()
v  = torch.randn(8, 32, 50).cuda()


__output__  = m(q, k, v)


