
class Model(torch.nn.Module):
    def __init__(self, query_embed_dim: int, key_embed_dim: int, value_embed_dim: int):
        super().__init__()
        self.q = torch.nn.Linear(query_embed_dim, query_embed_dim) # Linear layer that maps queries to query and keys
        self.k = torch.nn.Linear(key_embed_dim, key_embed_dim) # Linear layer that maps keys to query and keys
        self.v = torch.nn.Linear(value_embed_dim, value_embed_dim) # Linear layer that maps values to attention weights
        
        self.attn = None
 
    def forward(self, x):
        