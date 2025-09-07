
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, attn_dim, num_heads=1):
        super().__init__()
        self.query_dim  = query_dim
        self.key_dim    = key_dim
        self.attn_dim   = attn_dim
        self.num_heads  = num_heads
 
        self.w_q = torch.nn.Parameter(torch.randn(self.query_dim, self.key_dim) * math.sqrt(2.0 / (self.key_dim + self.query_dim)))
        self.w_k = torch.nn.Parameter(torch.randn(self.key_dim, self.key_dim) * math.sqrt(2.0 / (self.key_dim + self.query_dim)))
 
    def forward(self, x1, x2):
        # Compute dot products of query and key: kq
        w1 = torch.matmul(x1, self.w_k)
        w1  = torch.softmax(w1, dim=-1) * math.sqrt(1.0 / (self.key_dim + self.query_dim))
 
        # Compute the dot product of query and value: kq @ v
        kv = torch.matmul(x1, self.w_k)
        w2 = torch.softmax(kv, dim=-1) * math.sqrt(1.0 / (self.key_dim + self.query_dim))
 
        # Compute the scaled dot product of qk with mask: (qk + mask) @ v = kq @ v
        qv = x2 @ w2 + (w1 * torch.softmax(x2, dim=-1)  * math.sqrt(1.0 / (self.key_dim + self.query_dim)))
        return qv


# Initializing the model
m = Model(16, 32, 4)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
