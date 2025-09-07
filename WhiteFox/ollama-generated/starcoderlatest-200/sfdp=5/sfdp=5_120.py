
class Model(torch.nn.Module):
    def __init__(self, attn_dim=128):
        super().__init__()
        self.key = torch.nn.Linear(attn_dim, attn_dim)
        self.value = torch.nn.Linear(attn_dim, attn_dim)
 
    def forward(self, query, key, value, mask):
        # ... compute the dot product of query and key 