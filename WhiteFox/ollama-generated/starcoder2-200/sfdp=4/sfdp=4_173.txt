
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 3)
 
    def forward(self, query, key, value):
        v1  = query @ key.transpose(-2,-1)/math.sqrt(query.size(-1))
        v2  = v1 + attn_mask
        v3  = torch.softmax(v2, dim=-1)
        __output__  = v3 @ value
        return v4

# Initializing the model