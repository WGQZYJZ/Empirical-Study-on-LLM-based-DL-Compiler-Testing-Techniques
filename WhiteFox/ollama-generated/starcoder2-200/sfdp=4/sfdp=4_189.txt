
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 7)
 
    def forward(self, key):
        v1 = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v1 = v1 + attn_mask
        v3 = torch.softmax(v1, dim=-1)
        v4  = v3 @ value
