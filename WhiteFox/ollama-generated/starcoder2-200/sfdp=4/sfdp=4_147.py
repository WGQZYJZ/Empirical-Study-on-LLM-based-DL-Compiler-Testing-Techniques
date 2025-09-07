
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, attn_mask=None):
        v1  = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) 
        v3  = None
        if (attn_mask is not None) and ((v3 != 0)):
            v4 = attn_weight  = v1 + v3
            v5  = torch.softmax(v4, dim=-1)
        else:
            v2  = v1 + v3 # 5.2
            v5  = v1 @ v2
        return v5


# Initializing the model
m  = Model()

