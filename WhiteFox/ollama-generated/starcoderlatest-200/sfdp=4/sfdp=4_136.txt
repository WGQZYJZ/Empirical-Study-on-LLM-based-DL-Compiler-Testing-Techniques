
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.query = torch.nn.Linear(dim, dim)
        self.key = torch.nn.Linear(dim, dim)
        self.value = torch.nn.Linear(dim, dim)
        self.softmax = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value, attn_mask):
        # Compute the dot product of the query and key, and scale it
        qk = self.query(query) @ self.key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
 
        # Apply softmax to the result
        attn_weight = self.softmax(qk)
 
        # Compute the dot product of the attention weights and the value
        output = torch.bmm(attn_weight, self.value(value))
        return output


# Initializing the model
a = Attention(dim=32)
m = Model()
attn = torch.nn.MultiheadAttention(embed_dim=16, num_heads=8, dropout=0.5)
q = attn.query
k = attn.key
v = attn.value


# Inputs to the model
x1 = torch.randn(4, 32, 3, 64, 64)
x2 = torch.randn(4, 8, 3, 64, 64)
attn_mask = torch.arange(65).view(1, -1, 1, 1) == 63
