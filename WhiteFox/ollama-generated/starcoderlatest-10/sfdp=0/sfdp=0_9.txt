
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim):
        super().__init__()
 
        self.attention = torch.nn.MultiheadAttention(num_heads=2, dim_per_head=64)
 
        self.query = torch.nn.Linear(query_dim, 8 * 3 * 3, bias=False)
        self.key = torch.nn.Linear(key_dim, 8 * 3 * 3, bias=False)
 
    def forward(self, qk1):
        v1 = self.attention(qk1, qk1, qk1)[0]
 
        v2 = v1 / math.sqrt(v1.size(-1))
 
        return v2
 

# Initializing the model with the correct query_dim and key_dim
m = Model(query_dim=8 * 3 * 3, key_dim=8 * 3 * 3)

 # Inputs to the model
qk1 = torch.randn(64, 8 * 3 * 3, 64, 64)
