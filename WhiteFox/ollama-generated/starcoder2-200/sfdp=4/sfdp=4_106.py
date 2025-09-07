
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask):
        v1  = torch.bmm(query, key) / math.sqrt(query.size(-1)) + attn_mask 
        v2  = torch.softmax(v1, dim=-1)
        v3  = torch.bmm(v2, query)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
query  = torch.randn(8, 4096, 768)
key    = torch.randn(128, 512, 768)
attn_mask=torch.randn(128,)
attn_mask=-999 * torch.ones_like(attn_mask)
attn_mask=attn_mask.masked_fill((attn_mask < 0), -999).unsqueeze(-1).repeat(1, 512, 1)


# Outputs of the model
