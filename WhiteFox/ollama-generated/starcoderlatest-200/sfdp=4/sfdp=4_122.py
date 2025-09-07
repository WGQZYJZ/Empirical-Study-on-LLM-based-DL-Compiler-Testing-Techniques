
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_query = torch.nn.Linear(64, 512)
        self.attn_key   = torch.nn.Linear(64, 512)
 
    def forward(self, query, key, attn_mask=None):
        v1 = self.attn_query(query)
        v2 = self.attn_key(key)
        qk  = v1 @ v2.transpose(-2, -1) / math.sqrt(v1.size(-1))
        qk += attn_mask if attn_mask is not None else None
        qk = torch.softmax(qk, dim=-1)
        output  = qk @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
query   = torch.randn(1, 64, 64)
key     = torch.randn(1, 64, 64)
attn_mask = torch.eye(512).unsqueeze(0).repeat(3, 1, 1)


